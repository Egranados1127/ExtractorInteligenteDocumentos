import sys
sys.path.insert(0, r'c:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\MIAppExtraccion')
from app import ocr_imagen
from PIL import Image

img_path = r'C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-08 at 8.09.55 PM.jpeg'
img = Image.open(img_path)
texto = ocr_imagen(img)

texto_upper = texto.upper()

print('=== DEBUG DETECCIÓN ===')
print('Contiene DE 1 A 30:', 'DE 1 A 30' in texto_upper)
print('Contiene DE 31 A 60:', 'DE 31 A 60' in texto_upper)
print('Contiene PROVEEDOR:', 'PROVEEDOR' in texto_upper)
print()

# Buscar variantes
print('=== VARIANTES ===')
variantes = ['DE1A30', 'DE 1A30', 'DE1 A30', 'DE 1 A 30', 'De 1 a 30', 'De1a30']
for var in variantes:
    print(f'{var}: {var.upper() in texto_upper}')

print()
print('=== PRIMERAS 50 LÍNEAS DEL OCR ===')
lineas = texto.split('\n')
for i, linea in enumerate(lineas[:50], 1):
    print(f'{i:3}: {linea}')
