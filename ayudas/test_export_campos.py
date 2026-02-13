import sys
from app import extraer_datos, ocr_pdf_bytes

pdf_path = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\18773897.pdf"
with open(pdf_path, "rb") as f:
    texto = ocr_pdf_bytes(f.read(), max_paginas=1, dpi=200)
    datos, tablas = extraer_datos(texto, "18773897.pdf")

print("=" * 80)
print("ANÁLISIS DE CAMPOS PARA EXPORTACIÓN")
print("=" * 80)
print(f"Total de claves en datos: {len(datos)}")
print()

# Simular lo que hace la pestaña de exportación
campos_disponibles = [k for k in datos.keys() if not k.startswith('_')]
print(f"Campos disponibles para exportar (sin _): {len(campos_disponibles)}")
print()
print("Lista de campos disponibles:")
print("-" * 80)
for i, campo in enumerate(sorted(campos_disponibles), 1):
    valor = datos[campo]
    if len(str(valor)) > 50:
        valor_mostrar = str(valor)[:50] + "..."
    else:
        valor_mostrar = valor
    print(f"{i:2d}. {campo:30s} : {valor_mostrar}")
print()

# Ver si hay campos con _
campos_con_underscore = [k for k in datos.keys() if k.startswith('_')]
if campos_con_underscore:
    print("Campos con _ (excluidos de exportación):")
    for campo in campos_con_underscore:
        print(f"  - {campo}")
