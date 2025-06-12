
## 📄 Images & Document – Smart Text + Face Extractor

An intelligent, all-in-one API that handles various file types to extract text and detect faces – especially optimized for **CNICs, identity cards, and scanned documents**.

![Preview](snapshots/FrontCNICdataExtraction.PNG)
![Preview](snapshots/ImageTextExtraction.PNG)
![Preview](snapshots/RandomExcelFileExtraction.PNG)
![Preview](snapshots/pdfTextExtraction)
![Preview](snapshots/wordFileWithTextImage)

### 🚀 Key Features:

#### ✅ 1. **Multi-Format File Handling**

* Accepts:
  `JPG`, `JPEG`, `PNG`, `BMP`, `PDF`, `DOCX`, `XLS`, `XLSX`
* The API **automatically detects the file type** and processes it intelligently.
* No need to switch endpoints — it **processes all through a single API**.


#### ✅ 2. **Text Extraction + Face Detection**

* For any file containing images (direct or embedded):

  * 📝 Extracts text using **EasyOCR** with **English and Urdu support**.
  * 👤 Detects human face using **OpenCV**.
  * 🔄 Returns cropped face as **Base64-encoded image**.
* Ideal for processing **CNICs**, **passport photos**, or **official documents**.

---

#### ✅ 3. **Single Unified API Endpoint**

* Everything is handled via:

  POST /upload
  
* API Response includes:

  ```json
  {
    "Extracted_Text": "...",
    "Face_Image_Base64": "..."
  }
  ```
* Clean, fast, and efficient — perfect for **automation** or **document verification systems**.

---
*and also it have*:
**decode.py** file:
This utility script decodes a Base64 encoded image string (for example, the face image returned by the APIs) back into an image format usable for display or saving. It helps in converting the Base64 string back to a normal image for further processing or viewing.

### 🧠 Built With:

* **Python**
* **Flask**
* **OpenCV**
* **EasyOCR**
* **Filetype** (for type detection)
  
### 🧪 Use Cases:

* CNIC or ID Card Verification
* Document Scanning & Archiving
* Face-based Document Matching
* OCR for Urdu-English Documents


