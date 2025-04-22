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

def crop_to_paper_with_cane_highlight(image):
    """
    Devuelve:
    - La imagen recortada a la hoja
    - Una copia resaltada con la caña contorneada
    """
    contour = find_paper_contour(image)
    x, y, w, h = cv2.boundingRect(contour)
    cropped = image[y:y+h, x:x+w]

    # Detectar la caña con umbral
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Crear imagen debug con contornos verdes
    highlighted_debug = cropped.copy()
    cv2.drawContours(highlighted_debug, contours, -1, (0, 255, 0), 2)

    return cropped, highlighted_debug

def hay_cana(cropped_img, area_minima=1000, aspect_ratio_min=2.5, altura_relativa_min=0.3):
    """
    Verifica si hay al menos un objeto grande con forma alargada (caña) en la imagen recortada.
    """
    gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_h, img_w = gray.shape

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < area_minima:
            continue

        x, y, w, h = cv2.boundingRect(cnt)

        aspect_ratio = h / w if w > 0 else 0
        altura_relativa = h / img_h

        if aspect_ratio >= aspect_ratio_min and altura_relativa >= altura_relativa_min:
            return True

    return False