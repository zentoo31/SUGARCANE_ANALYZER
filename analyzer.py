import cv2
import os
from preprocessing import crop_to_paper
from measurement import get_pixel_per_cm, count_knots
from preprocessing import hay_cana
from preprocessing import crop_to_paper_with_cane_highlight

PAPER_WIDTH_CM = 164.0

def analizar_cana(image_path: str):
    image = cv2.imread(image_path)
    filename = os.path.basename(image_path)

    cropped, debug_cane = crop_to_paper_with_cane_highlight(image)
    if not hay_cana(cropped):
        raise ValueError("No se detectó una caña en la imagen.")
    pixel_per_cm = get_pixel_per_cm(cropped, PAPER_WIDTH_CM)
    length_cm = cropped.shape[0] / pixel_per_cm

    num_knots, knot_positions, distances_px = count_knots(
        cropped, debug=True, filename=filename
    )
    distances_cm = [d / pixel_per_cm for d in distances_px]

    # Guardar imagen con nudos marcados
    debug_knots = cropped.copy()
    for y in knot_positions:
        cv2.line(debug_knots, (0, y), (debug_knots.shape[1], y), (0, 0, 255), 2)

    output_path = os.path.join("output", f"nudos_{filename}")
    cv2.imwrite(output_path, debug_cane)

    return {
        "filename": filename,
        "length_cm": round(length_cm, 2),
        "num_knots": num_knots,
        "knot_thickness_cm": [round(d, 2) for d in distances_cm],
        "image_debug_url": f"/imagen/nudos_{filename}"
    }
