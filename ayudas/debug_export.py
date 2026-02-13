import sys
from app import extraer_datos, ocr_pdf_bytes

pdf_path = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\18773897.pdf"
with open(pdf_path, "rb") as f:
    texto = ocr_pdf_bytes(f.read(), max_paginas=1, dpi=200)
    datos, tablas = extraer_datos(texto, "18773897.pdf")

print("=" * 80)
print("DEBUG: VERIFICACIÓN DE CAMPOS")
print("=" * 80)
print(f"Tipo de datos: {type(datos)}")
print(f"Total claves en datos: {len(datos)}")
print()

# Simular exactamente lo que hace Streamlit en la pestaña Exportar
campos_disponibles = sorted([k for k in datos.keys() if not k.startswith("_")])
print(f"Campos disponibles para exportar (sin _): {len(campos_disponibles)}")
print()
print("Lista de campos:")
for i, campo in enumerate(campos_disponibles, 1):
    print(f"{i:2d}. {campo}")
