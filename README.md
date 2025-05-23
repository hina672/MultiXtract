🔹 1. Multi-Format File Handling
The API accepts images (jpg, jpeg, png, bmp, etc.), PDFs, Word (DOCX), and Excel (XLS/XLSX) files. It intelligently detects the file type and processes each format accordingly to extract content.

🔹 2. Text Extraction + Face Detection
For files containing images (or actual image files), it:

Extracts text using EasyOCR (supports English and Urdu).

Detects a human face using OpenCV, then returns the face image in base64 format.

🔹 3. Single Unified API Endpoint
Everything runs through one / POST endpoint, which returns:

"Extracted_Text" from the file/image

"Face_Image_Base64" (if a face is found in any image)

This makes the system a powerful and simple API for intelligent document/image processing.

