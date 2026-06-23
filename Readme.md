# 📄 DocuConvert – All-in-One Document Converter & OCR Platform

## 🚀 Project Overview

**DocuConvert** is a web-based document processing platform developed using Python and Streamlit that allows users to perform common document conversion and OCR (Optical Character Recognition) tasks from a single interface.

The project was created to eliminate the need for multiple software tools by providing document conversion and text extraction features in one easy-to-use platform.

The application supports image conversion, PDF processing, OCR-based text extraction, document transformation, and a responsive dashboard experience suitable for desktop and mobile devices.

---

## 🌐 Live Demo

> https://doc-converter.streamlit.app/


# ✨ Features

## 📷 Image to PDF Converter

### Supported Formats

* JPG
* JPEG
* PNG

### Functionality

* Upload image files
* Preview uploaded images
* Convert images into PDF
* Download generated PDF

### Library Used

```python
img2pdf
```

---

## 📄 PDF to JPG Converter

### Functionality

* Upload PDF file
* Render PDF pages
* Convert PDF page into JPG
* Preview generated image
* Download JPG output

### Current Version

* First-page conversion supported

### Future Enhancement

* Full multi-page image export

### Library Used

```python
pdf2image
```

---

## 📝 DOCX to PDF Converter

### Workflow

```text
DOCX
 ↓
LibreOffice (Headless Mode)
 ↓
PDF
```

### Benefits

* Better formatting preservation
* Open-source solution
* Local processing

---

## 📘 PDF to DOCX Converter

### Workflow

```text
PDF
 ↓
pdf2docx
 ↓
Editable DOCX
```

### Output

* Fully editable Word document

### Library Used

```python
pdf2docx
```

---

## 🔍 Image OCR

### Workflow

```text
Image
 ↓
Tesseract OCR
 ↓
Extracted Text
 ↓
Editable Text Area
 ↓
TXT Download
```

### Features

* OCR text extraction
* Editable output
* Download extracted text
* Fast processing

### Libraries Used

```python
pytesseract
Pillow
```

---

## 📑 PDF OCR

### Workflow

```text
PDF
 ↓
pdf2image
 ↓
Convert Pages to Images
 ↓
Tesseract OCR
 ↓
Merge Extracted Text
 ↓
Editable Text Area
 ↓
TXT Download
```

### Features

* Multi-page OCR support
* Editable extracted text
* TXT export functionality

---

# 🎨 User Interface

The application uses a completely customized Streamlit frontend rather than the default Streamlit layout.

## Dashboard Components

* Hero Section
* Feature Overview Cards
* Tool Cards
* Statistics Section
* Sidebar Navigation
* Footer Section

---

## Sidebar Navigation

Available Modules:

* Dashboard
* Image to PDF
* PDF to JPG
* DOCX to PDF
* PDF to DOCX
* Image OCR
* PDF OCR
* About
* How To Use

---

## 🌙 Theme System

### Implemented Themes

* Dark Theme
* Light Theme

### Features

* Theme Toggle
* Improved Accessibility
* Better User Experience

---

## 📱 Responsive Design

Designed for:

* Desktop
* Laptop
* Tablet
* Mobile

### UI Enhancements

* Gradient Backgrounds
* Modern Cards
* Hover Effects
* Responsive Layouts
* Professional Typography
* Alerts & Notifications
* Loading Indicators
* File Preview Components

---

# 🏗️ Project Architecture

## Folder Structure

```text
DocuConvert/
│
├── assets/
│   └── style.css
│
├── app.py
├── requirements.txt
├── packages.txt
```

---

# 🛠️ Tech Stack

| Category        | Technology                |
| --------------- | ------------------------- |
| Language        | Python                    |
| Framework       | Streamlit                 |
| OCR Engine      | Tesseract OCR             |
| PDF Rendering   | Poppler                   |
| DOCX Processing | python-docx               |
| PDF Conversion  | pdf2docx                  |
| Styling         | CSS                       |
| Deployment      | Streamlit Community Cloud |
| Version Control | Git & GitHub              |

---

# 📦 Python Dependencies

```text
streamlit
img2pdf
pdf2image
pytesseract
Pillow
pdf2docx
python-docx
```

---

# 🖥️ System Dependencies

## Tesseract OCR

Used for:

```text
Image OCR
PDF OCR
```

Install:

```bash
sudo apt install tesseract-ocr
```

---

## Poppler

Used for:

```text
PDF Rendering
PDF to Image Conversion
```

Install:

```bash
sudo apt install poppler-utils
```

---

## LibreOffice

Used for:

```text
DOCX ↔ PDF Conversion
```

Install:

```bash
sudo apt install libreoffice
```

---

# ⚙️ Installation Guide

## Clone Repository

```bash
git clone https://github.com/sahil-1819-r/Document-Converter

cd Document-Converter
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 📖 Usage Guide

## Image to PDF

1. Open Image to PDF section.
2. Upload JPG, JPEG, or PNG.
3. Preview image.
4. Click Convert.
5. Download PDF.

---

## PDF to JPG

1. Upload PDF.
2. Render page.
3. Convert to JPG.
4. Preview image.
5. Download JPG.

---

## DOCX to PDF

1. Upload DOCX.
2. Convert using LibreOffice.
3. Download PDF.

---

## PDF to DOCX

1. Upload PDF.
2. Convert document.
3. Download DOCX.

---

## Image OCR

1. Upload image.
2. Extract text.
3. Edit extracted text.
4. Download TXT file.

---

## PDF OCR

1. Upload PDF.
2. OCR processes all pages.
3. Combined text generated.
4. Edit text.
5. Download TXT output.

---

# 🚀 Deployment

## Platform

Streamlit Community Cloud

### Deployment Files

```text
requirements.txt
packages.txt
```

---

## packages.txt

```text
tesseract-ocr
poppler-utils
libreoffice
```

---

# 🔧 Development Journey

## Initial Version

Started with:

* Image to PDF
* PDF to JPG

---

## Gradual Improvements

Added:

* OCR Functionality
* PDF OCR
* DOCX Support
* Dashboard System
* Theme Support
* Navigation System
* Deployment Configuration

---

# 🤖 AI Usage Disclosure

This project was developed with AI assistance but is **not an AI-generated project**.

## How AI Was Used

### UI/UX Assistance

* Dashboard ideas
* Hero section concepts
* Layout suggestions
* Theme recommendations
* Responsive design planning

### Frontend Development Assistance

* CSS generation
* Styling improvements
* Layout optimization
* Theme implementation

### Code Refactoring

* Cleaner code structure
* Reusable component suggestions
* Error handling recommendations

### Debugging Assistance

* Streamlit issues
* Deployment errors
* OCR configuration problems
* Git and GitHub troubleshooting

### Documentation Assistance

* README drafting
* Feature descriptions
* Project explanation

---

## What Was Done Manually

The following tasks were completed manually:

* Application architecture design
* Feature integration
* Dependency management
* OCR workflow implementation
* Testing and validation
* GitHub repository setup
* Streamlit deployment
* Tesseract configuration
* LibreOffice configuration
* Debugging deployment issues
* Final UI decisions

AI assisted development, but implementation, integration, testing, deployment, and decision-making remained developer responsibilities.

---

# 💡 Skills Demonstrated

## Technical Skills

* Python Development
* Streamlit Development
* OCR Integration
* Document Processing
* File Handling
* PDF Manipulation
* Responsive UI Design
* CSS Customization
* Git
* GitHub
* Deployment
* Debugging
* Open Source Tool Integration

---

# 🔮 Future Enhancements

Planned upgrades include:

* Batch Conversion
* ZIP Downloads
* Multi-page Image Export
* Drag & Drop Workspace
* Conversion History
* User Authentication
* Cloud Storage Integration
* Resume Analyzer Module
* AI-powered Document Summarization
* Document Translation Support

---
