# Smart PDF Toolkit 🚀

Smart PDF Toolkit is a **free, offline, unlimited desktop application** for PDF organization and document conversion.  
It is designed for **real users**, with a strong focus on **privacy**, **simplicity**, and **practical everyday use**.

✅ No subscriptions  
✅ No login  
✅ No internet required  
✅ Unlimited conversions  
✅ Completely free  

Your files **never leave your system**.

---

## ✨ Why Smart PDF Toolkit?

Most online PDF tools:
- Upload your files to external servers
- Impose daily or monthly usage limits
- Require paid subscriptions
- Track user activity

**Smart PDF Toolkit does none of that.**

It is a **local desktop application** that works fully offline and provides a clean, step-by-step interface for common PDF tasks.

---

## 🧰 Features

### 📂 PDF Organization
- Merge multiple PDF files into a single PDF
- Split a PDF into individual pages

### 🔄 Convert to PDF
- Image → PDF
- Word → PDF
- PowerPoint → PDF

### 🔁 Convert from PDF
- PDF → Word (best-effort conversion for text-based PDFs)

---

## 🧭 How the Application Works

All tools follow the **same simple workflow**:

1. Select input file(s)
2. Choose output file name and location
3. Start processing
4. Track progress visually
5. Cancel the operation or return to Home anytime

Clear instructions are shown inside the application for each step.

---

## ⚙️ System Requirements

### For Users
- **Windows 10 / Windows 11 (64-bit)**
- **LibreOffice** (required for document conversions)

LibreOffice is used internally for Word, PowerPoint, and PDF conversions.

👉 Download LibreOffice:  
https://www.libreoffice.org/download/

---

## 📥 Installation

### Option 1: Use the Application (Recommended)

1. Download `SmartPDFToolkit.exe` (link provided in README or Releases)
2. Ensure **LibreOffice** is installed on your system
3. Double-click the EXE file to launch the application

✔ No Python installation required  
✔ No setup wizard  
✔ Works completely offline  

> Note: Windows may show an “Unknown Publisher” warning.  
> This is normal for unsigned desktop applications.

---

### Option 2: Run from Source Code (Developers)

```bash
pip install PyPDF2 pillow
python main.py
🛠 Build the Application (Developers)
To generate the Windows executable:

pyinstaller ^
 --onefile ^
 --windowed ^
 --name SmartPDFToolkit ^
 --add-data "ui;ui" ^
 --add-data "tools;tools" ^
 --add-data "utils;utils" ^
 main.py
The executable will be created inside the dist/ folder.

📁 Project Structure
SmartPDFToolkit/
├── src/            # Source code
│   ├── main.py
│   ├── ui/
│   ├── tools/
│   └── utils/
├── README.md
├── .gitignore
└── LICENSE
⚠️ Important Notes & Limitations
PDF → Word Conversion
Works best with text-based PDFs

Scanned or image-only PDFs may not convert correctly

Formatting quality depends on the original PDF and LibreOffice

The application silently converts whatever is possible and skips unsupported content without showing warnings.

🔐 Privacy & Security
All files are processed locally on your system

No internet connection is required

No analytics, tracking, or data collection

No files are stored or shared externally

Your documents remain private and secure.

🚀 Future Enhancements
PDF → Image conversion

Add page numbers

Add watermark

Dark mode UI

Installer (.msi / setup.exe)

📜 License
This project is free for personal and educational use.
No subscriptions. No hidden costs.

👤 Author
Developed by Darshan H V
Smart PDF Toolkit — v1.0
