import sys
from app import ocr_imagen
from PIL import Image
import os

# Buscar el archivo
base_path = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp"
archivos = os.listdir(base_path)
archivo_buscado = [f for f in archivos if "2026-01-31" in f and "12.53" in f]

if archivo_buscado:
    img_path = os.path.join(base_path, archivo_buscado[0])
    print(f"Archivo encontrado: {archivo_buscado[0]}")
    print("=" * 80)
    
    img = Image.open(img_path)
    print(f"Dimensiones: {img.size[0]}x{img.size[1]} px")
    print("=" * 80)
    print("TEXTO OCR EXTRAÍDO:")
    print("=" * 80)
    
    texto = ocr_imagen(img)
    print(texto)
    print("=" * 80)
    print(f"Total caracteres: {len(texto)}")
else:
    print("Archivo no encontrado. Archivos disponibles:")
    for f in archivos:
        if "WhatsApp" in f and "2026-01" in f:
            print(f"  - {f}")
