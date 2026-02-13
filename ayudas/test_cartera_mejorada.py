import sys
from app import extraer_datos, ocr_imagen
from PIL import Image

print('TEST: Cartera con coordenadas espaciales mejoradas')
print('=' * 80)

img_path = r'C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-08 at 8.09.55 PM.jpeg'

print('\n1. Cargando imagen...')
imagen = Image.open(img_path)
print(f'   Imagen cargada: {imagen.size[0]}x{imagen.size[1]} px')

print('\n2. Ejecutando OCR...')
texto = ocr_imagen(imagen)
print(f'   OCR completado: {len(texto)} caracteres')

print('\n3. Extrayendo datos con coordenadas espaciales...')
try:
    datos, tablas = extraer_datos(texto, 'cartera.jpeg', imagen)
    
    if isinstance(datos, dict) and '_tipo' in datos:
        filas = datos.get('_filas', [])
        print(f'\n   EXITO: Detectada tabla con {len(filas)} filas')
        
        if filas:
            print('\n' + '=' * 80)
            print('PRIMERAS 3 FILAS EXTRAIDAS:')
            print('=' * 80)
            
            for i, fila in enumerate(filas[:3], 1):
                print(f'\nFila {i}:')
                for col, valor in fila.items():
                    print(f'  {col:20s}: {valor}')
            
            print('\n' + '=' * 80)
            print('VERIFICACION DE COLUMNAS:')
            print('Las columnas deben tener valores correctos en cada posicion.')
            print('Si ves numeros en PROVEEDOR o nombres en TOTAL, hay un problema.')
            print('=' * 80)
    else:
        print(f'\n   ERROR: No se detecto como tabla')
        print(f'   Tipo: {type(datos)}')
        if isinstance(datos, dict):
            print(f'   Campos: {list(datos.keys())[:10]}')

except Exception as e:
    print(f'\nERROR: {e}')
    import traceback
    traceback.print_exc()
