# 🎥 Remove Watermark Auto

**Elimina marcas de agua en vídeos de forma automática y profesional con Python y OpenCV.**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux-orange.svg)](https://ubuntu.com)

---

## 🧠 Descripción

**Remove Watermark Auto** es un script profesional en **Python** diseñado para eliminar de forma automática **marcas de agua estáticas o móviles** en vídeos, manteniendo el **audio original** y sin utilizar modelos de IA pesados.

La herramienta utiliza **OpenCV** para rastrear el movimiento de la marca y aplicar **inpainting local** (reconstrucción inteligente del fondo), todo con una interfaz mínima y configurable por línea de comandos.

> 🎯 Ideal para sysadmins, creadores de contenido y profesionales IT que necesiten limpiar vídeos de forma rápida, reproducible y automatizada en sistemas **Linux**.

---

## 🎬 Vista previa / Demo

*(Ejemplo antes / después del procesamiento)*

> **[GIF o imagen aquí]**
> *Figura — Comparación antes/después del proceso de eliminación de marca de agua.*

---

## ⚙️ Características principales

✅ Rastreo automático de marcas mediante `cv2.legacy.TrackerCSRT_create()`
✅ Eliminación por **inpainting adaptativo (TELEA / NS)**
✅ Mantiene el **audio original** con FFmpeg
✅ Sin dependencias de IA ni procesamiento en la nube
✅ CLI profesional con control de parámetros (`-r`, `-o`, etc.)
✅ Barra de progreso en tiempo real con `tqdm`
✅ Compatible con cualquier vídeo en formato `.mp4`, `.avi`, `.mov`

---

## 🧩 Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/rafaelmperez/remove-watermark-auto.git
cd remove-watermark-auto

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r src/requirements.txt
```

Requisitos:

* Python 3.10+
* OpenCV (contrib)
* NumPy
* tqdm
* FFmpeg instalado en el sistema (`sudo apt install ffmpeg`)

---

## 🚀 Uso básico

```bash
python3 src/remove_watermark_auto.py ~/Escritorio/prueba1.mp4 -o output/prueba1_limpio.mp4
```

🧭 **Flujo del proceso:**

1. Se abre el primer frame del vídeo.
2. Seleccionas con el ratón la región donde se encuentra la marca.
3. El tracker sigue automáticamente la marca frame a frame.
4. El sistema reconstruye el fondo (inpainting) y elimina la marca.
5. Se genera un nuevo vídeo con el audio original restaurado.

---

## 📂 Estructura del proyecto

```
remove-watermark-auto/
├── src/
│   ├── remove_watermark_auto.py
│   ├── requirements.txt
│   └── README.md
├── output/
├── tests/
├── venv/
└── LICENSE
```

---

## 🧱 Arquitectura interna

| Módulo                | Descripción                                               |
| --------------------- | --------------------------------------------------------- |
| `extract_audio()`     | Extrae el audio original del vídeo mediante FFmpeg.       |
| `track_and_inpaint()` | Rastrea la marca y aplica reconstrucción del fondo.       |
| `merge_audio_video()` | Inserta nuevamente el audio en el vídeo procesado.        |
| `select_roi()`        | Permite al usuario definir la región inicial de la marca. |

🧠 **Algoritmos utilizados:**

* **CSRT Tracker:** seguimiento robusto de movimiento (ideal para marcas dinámicas).
* **Inpainting TELEA:** reconstrucción inteligente por difusión local.
* **FFmpeg Copy Stream:** mantiene el audio sin pérdida de calidad.

---

## ⚡ Rendimiento y limitaciones conocidas

| Caso                             | Resultado                   | Solución                                |
| -------------------------------- | --------------------------- | --------------------------------------- |
| Fondo uniforme / marca estática  | ✅ Perfecto                  | —                                       |
| Marca móvil / fondo dinámico     | ⚙️ Muy bueno                | Ajustar `-r` (radio de inpainting)      |
| Marca con transparencia variable | ⚠️ Artefactos leves         | Ejecutar doble pasada                   |
| Fondo con texto o detalle fino   | ⚠️ Posible distorsión local | Aumentar resolución antes del procesado |
| Vídeos muy comprimidos           | ⚠️ Bordes duros             | Reencodear con FFmpeg antes             |

🧩 *Consejo:*
Para vídeos complejos, usar:

```bash
python3 src/remove_watermark_auto.py video.mp4 -r 6
```

---

## 🧪 Ejemplo visual (demo simulada)

```text
🆕 Puerto abierto: 9929/tcp - Servicio: nping-echo
❌ Puerto cerrado: 8080/tcp - Servicio: http-proxy
🔁 Cambio: puerto 22/tcp cambió de OpenSSH 6.6 a OpenSSH 9.0
```

> Ejemplo visual de comparación frame a frame durante el proceso.

---

## 🔍 Palabras clave (SEO)

<!-- keywords: python opencv watermark removal video automation linux ffmpeg inpainting codebyralph rafaelmperez -->

Automatización en Linux · Procesamiento de vídeo · OpenCV avanzado · Ciberseguridad defensiva · Python CLI · Inpainting inteligente

---

## 👨‍💻 Autor

**Desarrollado por Rafael M. Pérez — [codebyRalph](https://www.github.com/rafaelmperez)**
🌐 [www.rafaelmperez.com](https://www.rafaelmperez.com)
🔗 [LinkedIn](https://www.linkedin.com/in/rafaelmperez)
✉️ [rmp.blueteam@proton.me](mailto:rmp.blueteam@proton.me)

> 💡 “Automatización defensiva, visión por computador y scripting profesional en Linux.”

---

## 🪪 Licencia

```
MIT License

Copyright (c) 2025 Rafael M. Pérez — codebyRalph
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
[...]
```

---

## ⭐ Recomendaciones

Si te ha sido útil:

* Dale una **estrella ⭐** al repositorio en GitHub.
* Compártelo con otros profesionales o equipos de IT.
* Contribuye con ideas o mejoras mediante Pull Requests.

