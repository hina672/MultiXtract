
## 📄 Images & Document – Smart Text + Face Extractor

An intelligent, all-in-one API that handles various file types to extract text and detect faces – especially optimized for **CNICs, identity cards, and scanned documents**.

Perfect Hina! Based on the image you shared and the file names in your GitHub `snapshots/` folder, here's the updated section of your `README.md` with all **📸 preview images** added properly:

---

### 📸 Sample Snapshots

#### 🖼️ Image Text Extraction

![Image Text](https://github.com/hina672/MultiXtract/raw/main/snapshots/Image%20Text%20Extraction.PNG)

---

#### 📊 Random Excel File Extraction

![Excel File](https://github.com/hina672/MultiXtract/raw/main/snapshots/Random%20excel%20file%20extraction.PNG)

---

#### 📄 PDF Text Extraction

![PDF](https://github.com/hina672/MultiXtract/raw/main/snapshots/pdfTextExtraction)

---

#### 📝 Word File with Text + Image Text Extraction

![Word File](https://github.com/hina672/MultiXtract/raw/main/snapshots/wordFileWithTextImage)

---



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

🔐 Note: This is a public demo overview. Preview images are intentionally excluded from this public demo to respect privacy and data sensitivity. The full source code is available upon request. Contact me via LinkedIn https://www.linkedin.com/in/hinaasad-/ or email at hinaasad672@gmail.com.
