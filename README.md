# 📱 Phone Number Extraction & WhatsApp Messaging System

This project is a web-based system that extracts phone numbers from **images and PDF files** using **OCR (Optical Character Recognition)** and automatically sends messages to those numbers through **WhatsApp Web automation**.

The system integrates **React frontend**, **Django backend**, **OCR processing**, and **Selenium automation**.

---

# 🚀 Features

- Extract phone numbers from **images**
- Extract phone numbers from **PDF documents**
- OCR-based text extraction
- Automatic **phone number detection**
- **Duplicate number removal**
- Send WhatsApp messages automatically
- Simple web interface for uploading files
- Single browser session for messaging

---

# 🛠 Technologies Used

### Frontend
- React.js
- HTML
- CSS
- JavaScript
- Axios

### Backend
- Python
- Django

### OCR Processing
- Tesseract OCR
- OpenCV

### Automation
- Selenium WebDriver

### Other Tools
- ChromeDriver
- WhatsApp Web

---

# 📂 Project Structure

```
project-folder
│
├── frontend (React build files)
│
├── backend
│   ├── views.py
│   ├── send_whatsapp.py
│   ├── ocr_utils.py
│   ├── number_extractor.py
│   └── excel_writer.py
│
├── media
│
├── chromedriver.exe
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙️ System Workflow

```
Upload Image / PDF
        ↓
OCR extracts text
        ↓
Phone numbers detected
        ↓
Duplicate numbers removed
        ↓
WhatsApp Web opened with Selenium
        ↓
Messages sent automatically
```

---

# 🖥 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/phone-number-extractor.git
cd phone-number-extractor
```

---

## 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Install Tesseract OCR

Download and install Tesseract OCR:

https://github.com/tesseract-ocr/tesseract

Add it to your **system PATH**.

---

## 4. Install ChromeDriver

1. Check your Chrome browser version
2. Download the matching ChromeDriver
3. Place `chromedriver.exe` in the project folder

---

# ▶️ Running the Project

Since the React frontend is already built and served by Django, **both frontend and backend run together**.

Run the project using **one terminal**:

```bash
python manage.py runserver
```

Then open:

```
http://127.0.0.1:8000
```

---

# 📲 WhatsApp Messaging Process

1. Upload an image or PDF containing phone numbers
2. System extracts numbers using OCR
3. Click **Send Messages**
4. WhatsApp Web opens
5. Scan QR code once
6. Messages are sent automatically to all extracted numbers

---

# ⚠️ Limitations

- Requires WhatsApp Web login
- Numbers must have active WhatsApp accounts
- Internet connection required
- Automation speed depends on browser performance

---

# 🔮 Future Improvements

- WhatsApp Business API integration
- Database storage for extracted numbers
- Contact name extraction
- Message scheduling
- Cloud deployment
- Improved OCR accuracy

---

## 👨‍💻 Author
Gabriel P SS  
AI & Data Engineering Intern

---

# 📜 License

This project is for **educational and research purposes only**.
README.md
Displaying README.md.