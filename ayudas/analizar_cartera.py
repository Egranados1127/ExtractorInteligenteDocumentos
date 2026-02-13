import sys
from app import extraer_datos, ocr_imagen
from PIL import Image

print('🔍 ANÁLISIS: WhatsApp Image 2026-01-08')
print('=' * 70)

# Cargar imagen de cartera
img_path = r'C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-08 at 8.09.55 PM.jpeg'
imagen = Image.open(img_path)
texto = ocr_imagen(imagen)

# Extraer datos
datos, tablas = extraer_datos(texto, 'cartera.jpeg', imagen)

print('\n📊 RESULTADO ACTUAL:')
print(f'   Tipo de datos: {type(datos).__name__}')
print(f'   Es diccionario: {isinstance(datos, dict)}')

if isinstance(datos, dict):
    tiene_tipo = '_tipo' in datos
    print(f'   Tiene campo "_tipo": {tiene_tipo}')
    
    if tiene_tipo:
        print(f'\n   ✅ _tipo: {datos.get("_tipo")}')
        print(f'   ✅ _filas: {len(datos.get("_filas", []))} filas detectadas')
        print(f'\n   RESULTADO: Solo tabla (CORRECTO)')
    else:
        print(f'\n   ❌ Campos individuales extraídos: {len(datos)}')
        print(f'   ❌ Primeros 10 campos: {list(datos.keys())[:10]}')
        print(f'\n   PROBLEMA: Extrayendo campos adicionales cuando solo debería ser tabla')

print(f'\n📋 Tablas adicionales en lista: {len(tablas) if tablas else 0}')

print('\n' + '=' * 70)
print('🎯 COMPORTAMIENTO ESPERADO (según PaddleOCR ejemplo):')
print('   ✅ Solo devolver: {"_tipo": "tabla_multiple", "_filas": [...]}')
print('   ✅ Filas con 8 columnas: DOCUMENTO, PROVEEDOR, CORRIENTE, 1-30, etc.')
print('   ❌ NO devolver: campos individuales como "Auto_Campo_1", etc.')
print('=' * 70)
