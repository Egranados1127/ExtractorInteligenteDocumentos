import sys
from app import extraer_datos, ocr_pdf_bytes

pdf_path = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\18773897.pdf"
with open(pdf_path, "rb") as f:
    texto = ocr_pdf_bytes(f.read(), max_paginas=1, dpi=200)
    datos, tablas = extraer_datos(texto, "18773897.pdf")

print("=" * 80)
print("DOCUMENTO HERINCO - 18773897.pdf")
print("=" * 80)
print(f"Total campos detectados: {len(datos)}")
print()
print("CAMPOS EXTRAÍDOS:")
print("-" * 80)
for clave, valor in sorted(datos.items()):
    print(f"{clave:30s} : {valor}")
print()
print(f"\n¿Cuántos campos esperabas? Dime cuáles faltan para agregarlos.")
