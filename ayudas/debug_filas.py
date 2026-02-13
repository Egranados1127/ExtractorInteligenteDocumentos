import sys
import re
from app import ocr_imagen
from PIL import Image

# Cargar imagen
img_path = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-31 at 12.53.22 PM.jpeg"
texto = ocr_imagen(Image.open(img_path))

# Eliminar encabezado
texto_limpio = re.sub(r'NOMBRE\s+ASESOR\s+PPTO\s+MES.*?MARGEN', '', texto, flags=re.IGNORECASE)

print("=" * 80)
print("BÚSQUEDA DE FILAS CON NOMBRE + PORCENTAJE DE MARGEN")
print("=" * 80)

# Buscar todas las líneas que tengan un nombre seguido de un porcentaje
patron_debug = re.compile(
    r'([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s\.&\(\)]{3,}?)\s*'  # Nombre
    r'.*?'  # Cualquier cosa en el medio
    r'(\d{1,3}(?:\.\d{1,2})?%)',  # Porcentaje (posible margen)
    re.IGNORECASE
)

coincidencias = list(patron_debug.finditer(texto_limpio))
print(f"Total de posibles filas encontradas: {len(coincidencias)}\n")

for i, match in enumerate(coincidencias[:20], 1):  # Mostrar primeras 20
    nombre = match.group(1).strip()
    porcentaje = match.group(2)
    contexto = match.group(0)[:100]
    print(f"{i}. {nombre} ... {porcentaje}")
    if len(contexto) < 100:
        print(f"   Contexto: {contexto}")
    else:
        print(f"   Contexto: {contexto}...")
    print()
