
# CamGuard

CamGuard is a Python-based real-time video analysis tool that uses OCR and an AI language model to simulate security guard reasoning. It captures video from your webcam, extracts visible text using OCR, and asks an LLM how to respond to the observed scenario. The result is overlaid on the video feed.

---

## 🔍 Features

- 🎥 **Real-Time Webcam Monitoring** using OpenCV
- 🧠 **Text Extraction with OCR** via Tesseract
- 🤖 **AI-Based Security Advice** using OpenAI's GPT-4o-mini
- 🖥️ **Live Visual Feedback** with overlayed text and responses
- 📦 **Modular Codebase** with clear separation of concerns

---

## 🧰 Technologies Used

- **Python 3.7+**
- **OpenCV** – Webcam capture and frame handling
- **pytesseract** – Python binding for Tesseract OCR
- **OpenAI API** – For LLM-based reasoning
- **python-dotenv** – Securely manage API keys and secrets

---

## 🗂️ Project Structure

```bash
.
├── camguard.py       # Main loop: video capture, OCR, and LLM integration
├── ocr.py            # Image preprocessing & text extraction
├── llm.py            # Query OpenAI model with extracted text
├── utils.py          # Utility for overlaying text on video frames
└── README.md         # Project overview and instructions
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/CamGuard.git
cd CamGuard
```

### 2. Set up the environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Install Tesseract
- **Windows**: [Download Tesseract](https://github.com/tesseract-ocr/tesseract)
  - Update `camguard.py` with the correct installation path:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```

- **Linux/macOS**:
  ```bash
  sudo apt install tesseract-ocr
  ```

### 4. Add your OpenAI API Key
Create a `.env` file:
```env
OPENAI_API_KEY=your_openai_key_here
```

---

## 🚀 Running the App

```bash
python camguard.py
```

- `Enter` → Sends the current OCR'd text to the LLM for analysis
- `q` → Quit the application

---

## 🧪 Example Use Case

Imagine you're monitoring a facility entrance. A sign appears with suspicious or important text. CamGuard extracts the text and queries the LLM like this:

**OCR'd Text**:
```
Unauthorized entry is prohibited. Violators will be reported.
```

**LLM Prompted Response**:
> "Ensure the entrance is monitored, verify the identity of individuals approaching, and alert security staff if any unauthorized person attempts entry."

---

## 📝 To Do / Improvements

- Add voice feedback
- Improve frame processing performance
- Integrate image classification (e.g., detect people, signs)

---

## 📜 License

This project is for educational and experimental use. All trademarks and technologies are property of their respective owners.

---