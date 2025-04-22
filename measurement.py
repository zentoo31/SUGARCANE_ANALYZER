import cv2
import numpy as np
from scipy.signal import find_peaks
import os
import matplotlib.pyplot as plt

def get_pixel_per_cm(cropped_img, real_width_cm):
    height, width = cropped_img.shape[:2]
    return width / real_width_cm

def count_knots(image, debug=False, merge_distance=100, filename="debugs"):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perfil vertical
    profile = np.sum(gray, axis=1).astype(np.float32)
    profile_2d = profile.reshape(-1, 1)
    profile_blurred = cv2.GaussianBlur(profile_2d, (9, 9), 0)
    profile_smooth = profile_blurred.flatten()

    # Picos en el perfil invertido (valles)
    inverted = -profile_smooth
    raw_peaks, _ = find_peaks(inverted, distance=10, prominence=1000)

    # Agrupar picos cercanos para contar un solo nudo
    grouped_peaks = []
    if len(raw_peaks) > 0:
        grouped_peaks = [raw_peaks[0]]
        for p in raw_peaks[1:]:
            if p - grouped_peaks[-1] >= merge_distance:
                grouped_peaks.append(p)

    distances = []
    for i in range(1, len(grouped_peaks)):
        d = grouped_peaks[i] - grouped_peaks[i - 1]
        distances.append(d)
    
    # === Debug visual ===
    if debug and filename:
        os.makedirs("debugs", exist_ok=True)

        # 1. Gráfica de perfil con picos originales y agrupados
        plt.figure(figsize=(10, 5))
        plt.plot(profile_smooth, label='Perfil suavizado', color='gray')
        plt.plot(raw_peaks, profile_smooth[raw_peaks], "x", label='Picos crudos', color='blue')
        plt.plot(grouped_peaks, profile_smooth[grouped_peaks], "o", label='Nudos (agrupados)', color='red')
        plt.title("Perfil vertical y detección de nudos")
        plt.xlabel("Fila (Y)")
        plt.ylabel("Intensidad total")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"debugs/profile_{filename}.png")
        plt.close()

        # 2. Imagen con líneas rojas en cada nudo agrupado
        img_debug = image.copy()
        for y in grouped_peaks:
            cv2.line(img_debug, (0, y), (img_debug.shape[1], y), (0, 0, 255), 2)
        cv2.imwrite(f"debugs/nudos_{filename}", img_debug)

    return len(grouped_peaks), grouped_peaks, distances


def measure_length_cm(image, pixel_per_cm):
    height = image.shape[0]
    return height / pixel_per_cm
