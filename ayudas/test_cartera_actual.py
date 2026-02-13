import sys
from app import extraer_datos, ocr_imagen
from PIL import Image

print('EXTRACCION ACTUAL - WhatsApp Image 2026-01-08')
print('=' * 80)

img_path = r'C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-08 at 8.09.55 PM.jpeg'
imagen = Image.open(img_path)
texto = ocr_imagen(imagen)

try:
    datos, tablas = extraer_datos(texto, 'cartera.jpeg', imagen)
    
    if isinstance(datos, dict) and '_tipo' in datos:
        filas = datos.get('_filas', [])
        print(f'\nDetecto tabla con {len(filas)} filas')
        print('\nPRIMERAS 3 FILAS:')
        print('=' * 80)
        
        for i, fila in enumerate(filas[:3], 1):
            print(f'\nFila {i}:')
            for col, valor in fila.items():
                print(f'  {col:15s}: {valor}')
        
        print('\nPROBLEMA: Revisa si las columnas tienen valores mezclados')
    else:
        print(f'\nNo detecto como tabla')
        print(f'Tipo: {type(datos)}')
        print(f'Campos: {list(datos.keys())[:10]}')
        
except Exception as e:
    print(f'\nERROR: {e}')
    import traceback
    traceback.print_exc()
