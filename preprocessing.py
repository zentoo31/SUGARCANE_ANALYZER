import cv2
import numpy as np

def find_paper_contour(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    edged = cv2.Canny(blur, 50, 150)
    
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    paper_contour = max(contours, key=cv2.contourArea)
    
    return paper_contour

def crop_to_paper(image):
    contour = find_paper_contour(image)
    x, y, w, h = cv2.boundingRect(contour)
    return image[y:y+h, x:x+w]

def hay_cana(cropped_img, area_minima=1000):
    """
    Verifica si hay al menos un objeto grande (caña) en la imagen recortada.
    """
    gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > area_minima:
            return True
    return False