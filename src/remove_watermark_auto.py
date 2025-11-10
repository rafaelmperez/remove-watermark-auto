#!/usr/bin/env python3
"""
remove_watermark_auto.py
Autor: Rafael M. Pérez — codebyRalph
Descripción:
Elimina marcas de agua en vídeos (estáticas o en movimiento) mediante
selección de ROI + tracking + inpainting, conservando el audio original.
"""

import cv2
import numpy as np
import subprocess
import os
from tqdm import tqdm
import argparse
import tempfile

# -------------------------------------------------------
# FUNCIONES
# -------------------------------------------------------

def extract_audio(video_path, audio_path):
    """Extrae el audio original con FFmpeg."""
    subprocess.run([
        "ffmpeg", "-y", "-i", video_path, "-vn",
        "-acodec", "copy", audio_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def merge_audio_video(video_noaudio, audio_path, output_path):
    """Inserta nuevamente el audio original."""
    subprocess.run([
        "ffmpeg", "-y", "-i", video_noaudio, "-i", audio_path,
        "-c", "copy", output_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def select_roi(video_path):
    """Muestra el primer frame para seleccionar el ROI con el ratón."""
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("No se pudo leer el vídeo o está corrupto.")
    cv2.imshow("Selecciona la marca de agua y presiona ENTER", frame)
    roi = cv2.selectROI("Selecciona la marca de agua y presiona ENTER", frame, False)
    cv2.destroyAllWindows()
    cap.release()
    return roi  # (x, y, w, h)


def track_and_inpaint(video_path, roi, output_path, inpaint_radius=3):
    """Rastrea el ROI y aplica inpainting frame a frame."""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    tmp_video = output_path
    out = cv2.VideoWriter(tmp_video, fourcc, fps, (width, height))

    tracker = cv2.legacy.TrackerCSRT_create()
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("No se pudo leer el primer frame para el tracker.")
    tracker.init(frame, roi)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for _ in tqdm(range(total_frames), desc="Procesando frames", ncols=80):
        ret, frame = cap.read()
        if not ret:
            break

        success, box = tracker.update(frame)
        if success:
            x, y, w, h = map(int, box)
            mask = np.zeros(frame.shape[:2], dtype=np.uint8)
            cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
            frame = cv2.inpaint(frame, mask, inpaint_radius, cv2.INPAINT_TELEA)
        else:
            # Si se pierde el tracking, continuar con el ROI anterior
            x, y, w, h = map(int, roi)
            mask = np.zeros(frame.shape[:2], dtype=np.uint8)
            cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
            frame = cv2.inpaint(frame, mask, inpaint_radius, cv2.INPAINT_TELEA)

        out.write(frame)

    cap.release()
    out.release()


# -------------------------------------------------------
# MAIN
# -------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Eliminar marcas de agua (estáticas o móviles) en vídeo.")
    parser.add_argument("input", help="Ruta del vídeo de entrada.")
    parser.add_argument("-o", "--output", default="output_final.mp4", help="Nombre del archivo de salida.")
    parser.add_argument("-r", "--radius", type=int, default=3, help="Radio del inpainting (por defecto 3).")
    args = parser.parse_args()

    input_video = args.input
    output_video = args.output
    inpaint_radius = args.radius

    with tempfile.TemporaryDirectory() as tmpdir:
        audio_path = os.path.join(tmpdir, "audio.aac")
        tmp_noaudio = os.path.join(tmpdir, "tmp_noaudio.mp4")

        print("\n[1/4] Extrayendo audio original...")
        extract_audio(input_video, audio_path)

        print("[2/4] Selecciona la región de la marca de agua.")
        roi = select_roi(input_video)
        print(f"ROI seleccionado: {roi}")

        print("[3/4] Eliminando marca y generando vídeo...")
        track_and_inpaint(input_video, roi, tmp_noaudio, inpaint_radius=inpaint_radius)

        print("[4/4] Insertando audio original...")
        merge_audio_video(tmp_noaudio, audio_path, output_video)

    print(f"\n✅ Proceso completado. Archivo generado: {output_video}")


if __name__ == "__main__":
    main()
