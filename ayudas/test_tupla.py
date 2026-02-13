import sys
from app import extraer_datos, ocr_imagen
from PIL import Image

# Probar con tabla de 2 columnas
img_path = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-28 at 8.02.20 AM.jpeg"
texto = ocr_imagen(Image.open(img_path))

# Esta llamada debe retornar una tupla (datos, tablas)
resultado = extraer_datos(texto, "WhatsApp Image 2026-01-28.jpeg")

print(f"Tipo de resultado: {type(resultado)}")
print(f"Es tupla?: {isinstance(resultado, tuple)}")

if isinstance(resultado, tuple):
    datos, tablas = resultado
    print(f" Retorna tupla correctamente")
    print(f"  - Tipo de datos: {type(datos)}")
    print(f"  - Tipo de tablas: {type(tablas)}")
    
    if isinstance(datos, dict) and "_tipo" in datos:
        print(f"  - _tipo: {datos.get('_tipo')}")
        print(f"  - Filas: {len(datos.get('_filas', []))}")
    else:
        print(f"  - Campos normales: {len(datos)}")
else:
    print(" NO retorna tupla")
