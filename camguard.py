import cv2
import pytesseract
import time

from ocr import extract_text, preprocess_image
from llm import query_llm
from utils import overlay_text

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Unable to open webcam. Please check your connection.")
        return

    current_text = ""
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        processed_image = preprocess_image(frame)
        
        extracted_text = extract_text(processed_image).strip()
        if extracted_text and extracted_text != current_text:
            current_text = extracted_text
            print("OCR Text:", current_text)

        if current_text:
            overlay_text(frame, "Detected Text: " + current_text, position=(30, 60))
            overlay_text(frame, "Press Enter to analyze the text. Press 'q' to quit.", position=(30, 30))
        
        cv2.imshow("CamGuard AI", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == 13 and current_text:
            prompt = (
                f"Imagine you are a security guard and you observe the following event:\n\n"
                f"\"{current_text}\"\n\n"
                "What actions would you take to ensure safety and what precautions would you implement?"
            )
            response = query_llm(prompt)
            print("LLM Response:", response)
            overlay_text(frame, "LLM Response: " + response, position=(30, 90))
            time.sleep(2)
        elif key == ord('q'):
            break

        time.sleep(0.1)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()