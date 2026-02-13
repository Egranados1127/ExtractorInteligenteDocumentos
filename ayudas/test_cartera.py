import sys
sys.path.insert(0, r'c:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\MIAppExtraccion')
from app import extraer_datos, ocr_imagen
from PIL import Image

# Procesar imagen de cartera por edades
img_path = r'C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-08 at 8.09.55 PM.jpeg'
img = Image.open(img_path)
texto = ocr_imagen(img)

# Ejecutar extracción
resultado = extraer_datos(texto, 'WhatsApp Image 2026-01-08.jpeg')

if isinstance(resultado, tuple):
    datos, tablas_genericas = resultado
    
    if isinstance(datos, dict) and '_tipo' in datos and datos['_tipo'] == 'tabla_multiple':
        print('=' * 80)
        print('CARTERA POR EDADES - EXTRACCIÓN EXITOSA')
        print('=' * 80)
        print(f'Total filas detectadas: {len(datos["_filas"])}')
        print()
        
        # Mostrar primeras 10 filas
        print('--- PRIMERAS 10 FILAS ---')
        for i, fila in enumerate(datos['_filas'][:10], 1):
            print(f'\nFila {i}:')
            for clave, valor in fila.items():
                print(f'  {clave}: {valor}')
        
        print()
        print('--- ÚLTIMAS 5 FILAS ---')
        for i, fila in enumerate(datos['_filas'][-5:], len(datos['_filas'])-4):
            print(f'\nFila {i}:')
            for clave, valor in fila.items():
                print(f'  {clave}: {valor}')
        
        print()
        print('=' * 80)
        print(f'RESUMEN: {len(datos["_filas"])} proveedores con cartera detectados')
        print('=' * 80)
    else:
        print('❌ No se detectó como tabla de cartera por edades')
        print(f'Tipo: {type(datos)}')
        if isinstance(datos, dict):
            print(f'Claves: {list(datos.keys())[:10]}')
else:
    print('❌ Resultado no es una tupla')
