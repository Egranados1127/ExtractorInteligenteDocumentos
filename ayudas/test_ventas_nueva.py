import sys
from app import extraer_datos, ocr_imagen
from PIL import Image
import os

# Cargar el archivo
img_path = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-31 at 12.53.22 PM.jpeg"
img = Image.open(img_path)
texto = ocr_imagen(img)

# Extraer datos
datos, tablas = extraer_datos(texto, "WhatsApp Image 2026-01-31.jpeg")

print("=" * 80)
print("RESULTADOS ACTUALES")
print("=" * 80)

if datos.get("_tipo") == "tabla_multiple":
    filas = datos.get("_filas", [])
    print(f"Tipo: Tabla múltiple")
    print(f"Filas detectadas: {len(filas)}")
    print()
    print("Filas extraídas:")
    for i, fila in enumerate(filas, 1):
        print(f"\n{i}. {fila.get('NOMBRE ASESOR', 'N/A')}")
        for key, val in fila.items():
            if key != 'NOMBRE ASESOR':
                print(f"   {key}: {val}")
else:
    print(f"Tipo: Documento normal")
    print(f"Campos: {len(datos)}")
