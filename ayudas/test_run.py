import sys
from app import extraer_datos, ocr_imagen
from PIL import Image

img_path = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-31 at 12.53.22 PM.jpeg"
texto = ocr_imagen(Image.open(img_path))
resultado = extraer_datos(texto, "WhatsApp Image 2026-01-31.jpeg")

print("=== RESULTADO TABLA VENTAS ===")
print(f"Tipo: {resultado.get('_tipo', 'normal')}")
print(f"Total filas: {len(resultado.get('_filas', []))}")
print()
print("FILA | NOMBRE ASESOR                        | PPTO MES         | PPTO FECHA       | VALOR VENTAS     | % CUMPL  | % MARG")
print("-" * 130)
for i, f in enumerate(resultado.get('_filas', []), 1):
    print(f"{i:3d}  | {f['NOMBRE ASESOR'][:35]:35s} | {f['PPTO MES']:16s} | {f['PPTO A LA FECHA']:16s} | {f['VALOR VENTAS']:16s} | {f['% CUMPLIMIENTO']:8s} | {f['% MARGEN']}")
