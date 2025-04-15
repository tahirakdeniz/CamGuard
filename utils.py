import cv2

def overlay_text(image, text, position=(10, 30), font_scale=0.7, color=(0, 255, 0), thickness=2):
    cv2.putText(image, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness, cv2.LINE_AA)
