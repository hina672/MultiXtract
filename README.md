
## 📄 Images & Document – Smart Text + Face Extractor

An intelligent, all-in-one API that handles various file types to extract text and detect faces – especially optimized for **CNICs, identity cards, and scanned documents**.


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


