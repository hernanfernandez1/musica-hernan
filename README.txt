StemGame v2
===========

REQUISITOS
----------
- Python 3.11 instalado
- ffmpeg.exe, ffprobe.exe, ffplay.exe en la misma carpeta

PASOS
-----
1. Pone todos los archivos en una carpeta (ej: D:\stemgame\)
2. Copia ffmpeg.exe, ffprobe.exe, ffplay.exe a esa carpeta
3. Abre consola en esa carpeta
4. Ejecuta:  py -3.11 descargar.py
5. Cuando termine, ejecuta:  py -3.11 -m http.server 8080
6. Abre Chrome en:  http://localhost:8080

NOVEDADES v2
------------
- Descarga solo 30 segundos por cancion (mucho mas rapido)
- Guarda progreso mientras procesa (podes jugar antes de terminar)
- Mas estable en Windows
