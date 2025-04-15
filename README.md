# CamGuard

## Overview

CamGuard is a Python-based security tool that leverages computer vision and natural language processing to analyze real-time events captured by your webcam. The application processes live video feeds, extracts text from captured frames using OCR, and then queries a language model to generate actionable security advice. This project is ideal for educational and experimental purposes, demonstrating how to integrate multiple libraries—OpenCV, Tesseract OCR, and the OpenAI API—into a single security-oriented application.

## Features

- **Real-Time Video Capture:** Uses OpenCV to access the webcam and process live video streams.  
  :contentReference[oaicite:0]{index=0}&#8203;:contentReference[oaicite:1]{index=1}

- **Optical Character Recognition (OCR):** Preprocesses video frames and extracts text using Tesseract via the pytesseract library.  
  :contentReference[oaicite:2]{index=2}&#8203;:contentReference[oaicite:3]{index=3}

- **LLM-Integrated Security Analysis:** Sends extracted text as a prompt to a language model (using the OpenAI API) to obtain security recommendations, simulating the response of an experienced security guard.  
  :contentReference[oaicite:4]{index=4}&#8203;:contentReference[oaicite:5]{index=5}

- **On-Screen Overlays:** Provides real-time visual feedback by overlaying detected text and instructions on the video feed.  
  :contentReference[oaicite:6]{index=6}&#8203;:contentReference[oaicite:7]{index=7}

## Technologies

- **Python 3.7+**
- **OpenCV:** For video capture and frame processing.
- **Tesseract OCR & pytesseract:** For extracting text from video frames.
- **OpenAI API:** For querying the language model.
- **dotenv:** For managing environment variables securely.

## File Structure

- **camguard.py:**  
  The main application file. It captures video from the webcam, performs OCR on each frame, overlays text and instructions on the video feed, and interacts with the language model when prompted.  
  :contentReference[oaicite:8]{index=8}&#8203;:contentReference[oaicite:9]{index=9}

- **ocr.py:**  
  Contains functions to preprocess images and extract text using Tesseract OCR.  
  :contentReference[oaicite:10]{index=10}&#8203;:contentReference[oaicite:11]{index=11}

- **llm.py:**  
  Provides the function to query the language model using the OpenAI API.  
  :contentReference[oaicite:12]{index=12}&#8203;:contentReference[oaicite:13]{index=13}

- **utils.py:**  
  Includes utility functions such as overlaying text on an image frame.  
  :contentReference[oaicite:14]{index=14}&#8203;:contentReference[oaicite:15]{index=15}

- **README.md:**  
  This file.

## Prerequisites

Before running CamGuard, ensure the following are installed and configured:

1. **Python 3.7 or Newer:**  
   Make sure your Python environment meets this requirement.

2. **Tesseract OCR:**  
   Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).  
   For Windows users, update the Tesseract path in `camguard.py`:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'