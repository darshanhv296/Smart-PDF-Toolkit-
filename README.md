# Smart PDF Toolkit 🚀

Smart PDF Toolkit is a **free, offline, unlimited desktop application** for PDF organization and document conversion.  
It is built for **real users**, **privacy**, and **practical everyday use**.

✅ No subscriptions  
✅ No login  
✅ No internet required  
✅ Unlimited conversions  
✅ Completely free  

Your files never leave your system.

---

## ✨ Why Smart PDF Toolkit?

Most online PDF tools:
- Upload your files to servers
- Limit conversions
- Require subscriptions
- Track user activity

**Smart PDF Toolkit does none of that.**

It is a **local desktop application** designed to work fully offline with a clean, step-by-step interface.

---

## 🧰 Features

### 📂 PDF Organization
- Merge multiple PDF files into one
- Split a PDF into individual pages

### 🔄 Convert to PDF
- Image → PDF
- Word → PDF
- PowerPoint → PDF

### 🔁 Convert from PDF
- PDF → Word (best-effort, text-based PDFs)

---

## 🧭 How the App Works

All tools follow the **same simple workflow**:

1. Select input file(s)
2. Choose output file name and location
3. Start processing
4. Track progress visually
5. Cancel or return home anytime

Clear instructions are shown inside the app for every step.

---

## ⚙️ System Requirements

### Required (Users)
- **Windows 10 / Windows 11 (64-bit)**
- **LibreOffice** (must be installed)

LibreOffice is used internally for Word, PowerPoint, and PDF conversions.

👉 Download LibreOffice:  
https://www.libreoffice.org/download/

---

## 📥 Installation

### Option 1: Use the Application (Recommended)

1. Go to the `app/` folder
2. Download `SmartPDFToolkit.exe`
3. Ensure **LibreOffice** is installed
4. Double-click the EXE to start

✔ No Python required  
✔ No setup wizard  
✔ No internet required  

---

### Option 2: Run from Source Code (Developers)

```bash
pip install PyPDF2 pillow
python main.py
```

---

## 🛠 Build the Application (Developers)

```bash
pyinstaller ^
 --onefile ^
 --windowed ^
 --name SmartPDFToolkit ^
 --add-data "ui;ui" ^
 --add-data "tools;tools" ^
 --add-data "utils;utils" ^
 main.py
```

---

## 📁 Project Structure

```
SmartPDFToolkit/
├── src/
├── app/
├── README.md
└── .gitignore
```

---

## ⚠️ Important Notes & Limitations

### PDF → Word Conversion
- Works best with **text-based PDFs**
- Scanned PDFs may not convert correctly
- Formatting depends on LibreOffice

The application silently converts whatever is possible.

---

## 🔐 Privacy & Security

- Files processed locally
- No internet connection required
- No tracking or analytics

---

## 🚀 Future Enhancements

- PDF → Image
- Add page numbers
- Add watermark
- Dark mode UI

---

## 📜 License

Free for personal and educational use.

---

## 👤 Author

Developed by **Darshan H V**  
Smart PDF Toolkit — v1.0
