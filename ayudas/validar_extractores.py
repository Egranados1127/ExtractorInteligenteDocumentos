import sys
from app import extraer_datos, ocr_pdf_bytes, ocr_imagen
from PIL import Image

print("=" * 80)
print("VALIDACIÓN DE EXTRACTORES ESPECIALIZADOS")
print("=" * 80)

# 1. HERINCO - 18773897.pdf
print("\n1. DOCUMENTO HERINCO (18773897.pdf)")
print("-" * 80)
pdf_path = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\18773897.pdf"
with open(pdf_path, "rb") as f:
    texto_herinco = ocr_pdf_bytes(f.read(), max_paginas=1, dpi=200)
    datos_herinco = extraer_datos(texto_herinco, "18773897.pdf")

print(f"Total campos: {len(datos_herinco)}")
print(f"Campos esperados: 27")
print(f"Estado: {' EXITOSO' if len(datos_herinco) == 27 else ' REVISAR'}")
print("\nPrimeros 5 campos:")
for k, v in list(datos_herinco.items())[:5]:
    print(f"  {k}: {v}")

# 2. VISION INTEGRADOS - FORMULA.pdf
print("\n\n2. DOCUMENTO VISION INTEGRADOS (FORMULA.pdf)")
print("-" * 80)
pdf_path2 = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\FORMULA.pdf"
with open(pdf_path2, "rb") as f:
    texto_vision = ocr_pdf_bytes(f.read(), max_paginas=1, dpi=200)
    datos_vision = extraer_datos(texto_vision, "FORMULA.pdf")

print(f"Total campos: {len(datos_vision)}")
print(f"Campos esperados: 33")
print(f"Estado: {' EXITOSO' if len(datos_vision) >= 32 else ' REVISAR'}")
print("\nPrimeros 5 campos:")
for k, v in list(datos_vision.items())[:5]:
    print(f"  {k}: {v}")

# 3. TABLA DOS COLUMNAS - WhatsApp Image 2026-01-28
print("\n\n3. TABLA DOS COLUMNAS (WhatsApp Image 2026-01-28)")
print("-" * 80)
img_path = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-28 at 8.02.20 AM.jpeg"
texto_tabla = ocr_imagen(Image.open(img_path))
datos_tabla = extraer_datos(texto_tabla, "WhatsApp Image 2026-01-28.jpeg")

if datos_tabla.get("_tipo") == "tabla_multiple":
    filas = datos_tabla.get("_filas", [])
    print(f"Tipo: tabla_multiple")
    print(f"Total filas: {len(filas)}")
    print(f"Filas esperadas: ~20")
    print(f"Estado: {' EXITOSO' if len(filas) >= 18 else ' REVISAR'}")
    print("\nPrimeras 3 filas:")
    for i, fila in enumerate(filas[:3], 1):
        print(f"  {i}. {fila['NOMBRE RUT'][:30]:30s} -> {fila['NOMBRE COMERCIAL'][:30]}")
else:
    print(" NO DETECTADO COMO TABLA MÚLTIPLE")

print("\n" + "=" * 80)
print("RESUMEN")
print("=" * 80)
print(f"1. HERINCO: {len(datos_herinco)} campos")
print(f"2. VISION INTEGRADOS: {len(datos_vision)} campos")
print(f"3. TABLA 2 COLUMNAS: {len(datos_tabla.get('_filas', []))} filas")
