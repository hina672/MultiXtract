import base64
import fitz  
import cv2
import easyocr
import numpy as np
import pandas as pd
import docx
from io import BytesIO
from flask import Flask, request, jsonify
from PIL import Image

app = Flask(__name__)

reader = easyocr.Reader(['en', 'ur'])
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def image_to_base64(image_np):
    _, buffer = cv2.imencode('.jpg', image_np)
    return base64.b64encode(buffer).decode('utf-8')

def prepare_grayscale_image(image_np):
    try:
        if len(image_np.shape) == 2:  
            return image_np
        elif image_np.shape[2] == 3:
            return cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
        elif image_np.shape[2] == 4:
            image_rgb = cv2.cvtColor(image_np, cv2.COLOR_RGBA2RGB)
            return cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
        else:
            return image_np
    except:
        return image_np

def extract_text_and_face(image_np):
    extracted_text = "No text found"
    face_base64 = None

    try:
        gray = prepare_grayscale_image(image_np)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) > 0:
            x, y, w, h = faces[0]
            face_img = image_np[y:y+h, x:x+w]
            face_base64 = image_to_base64(face_img)

        results = reader.readtext(gray)
        if results:
            extracted_text = "\n".join([res[1] for res in results])

    except Exception as e:
        extracted_text = f"Error: {str(e)}"

    return extracted_text, face_base64

def extract_text_from_pdf(file_bytes):
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    all_text = []
    face_base64_list = []

    for page in doc:
        all_text.append(page.get_text("text"))
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_np = np.array(Image.open(BytesIO(image_bytes)))

            text, face = extract_text_and_face(image_np)
            all_text.append(text)
            if face:
                face_base64_list.append(face)

    return "\n".join(all_text[:500]), face_base64_list[0] if face_base64_list else None

def extract_text_from_docx(file_bytes):
    doc = docx.Document(BytesIO(file_bytes))
    all_text = []
    face_base64_list = []

    for para in doc.paragraphs:
        all_text.append(para.text)

    for rel in doc.part.rels:
        if "image" in doc.part.rels[rel].target_ref:
            image_data = doc.part.rels[rel].target_part.blob
            image_np = np.array(Image.open(BytesIO(image_data)))

            text, face = extract_text_and_face(image_np)
            all_text.append(text)
            if face:
                face_base64_list.append(face)

    return "\n".join(all_text[:500]), face_base64_list[0] if face_base64_list else None

def extract_text_from_excel(file_bytes):
    df = pd.read_excel(BytesIO(file_bytes), sheet_name=None, engine="openpyxl")
    all_text = []
    face_base64_list = []

    for sheet_name, sheet in df.items():
        all_text.append(f"Sheet: {sheet_name}")
        all_text.append(sheet.to_string(index=False, header=True))


    return "\n".join(all_text[:500]), None

@app.route('/', methods=['POST'])
def upload_and_process():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_bytes = file.read()
    file_ext = file.filename.split('.')[-1].lower()

    if file_ext in ["jpg", "jpeg", "png", "bmp", "tiff", "gif"]:
        image_np = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_COLOR)
        if image_np is None:
            return jsonify({"error": "Error decoding image"}), 400
        text, face = extract_text_and_face(image_np)

    elif file_ext == "pdf":
        text, face = extract_text_from_pdf(file_bytes)

    elif file_ext == "docx":
        text, face = extract_text_from_docx(file_bytes)

    elif file_ext in ["xls", "xlsx"]:
        text, face = extract_text_from_excel(file_bytes)

    else:
        return jsonify({"error": f"Unsupported file format: {file_ext}"}), 400

    result = {
        "Extracted_Text": text
    }
    if face:
        result["Face_Image_Base64"] = face

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
