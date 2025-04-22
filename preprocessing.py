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