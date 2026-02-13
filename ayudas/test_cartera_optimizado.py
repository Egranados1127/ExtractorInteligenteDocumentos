import sys
sys.path.insert(0, r'c:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\MIAppExtraccion')
from app import extraer_datos
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import os

os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_path = r'C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-08 at 8.09.55 PM.jpeg'
img = Image.open(img_path)

# Preprocesamiento agresivo
img = img.convert('L')  # Escala de grises
img = img.point(lambda x: 0 if x < 140 else 255, '1')  # Binarización agresiva
img = img.convert('L')
enhancer = ImageEnhance.Sharpness(img)
img = enhancer.enhance(2.0)

# Aumentar tamaño 1.5x
ancho, alto = img.size
img = img.resize((int(ancho * 1.5), int(alto * 1.5)), Image.Resampling.LANCZOS)

# OCR con configuración optimizada para tablas
config = '--psm 6 --oem 3'
texto = pytesseract.image_to_string(img, lang='spa', config=config)

print('=' * 80)
print('PROCESANDO CON OCR OPTIMIZADO PARA TABLAS')
print('=' * 80)

# Ejecutar extracción
resultado = extraer_datos(texto, 'WhatsApp Image 2026-01-08.jpeg')

if isinstance(resultado, tuple):
    datos, tablas_genericas = resultado
    
    if isinstance(datos, dict) and '_tipo' in datos and datos['_tipo'] == 'tabla_multiple':
        print(f'✅ Total filas detectadas: {len(datos["_filas"])}')
        print()
        
        # Mostrar primeras 5 filas completas
        print('--- PRIMERAS 5 FILAS ---')
        for i, fila in enumerate(datos['_filas'][:5], 1):
            print(f'\nFila {i}:')
            for clave, valor in fila.items():
                print(f'  {clave}: {valor}')
        
        # Contar columnas con datos
        columnas_con_datos = {}
        for fila in datos['_filas']:
            for col in ['Corriente', 'De 1 a 30', 'De 31 a 60', 'De 61 a 90', 'De 91 o mas', 'Total']:
                if fila[col] not in ['$0.00', '', '$']:
                    columnas_con_datos[col] = columnas_con_datos.get(col, 0) + 1
        
        print()
        print('=== RESUMEN DE COLUMNAS ===')
        for col, count in columnas_con_datos.items():
            print(f'{col}: {count} filas con datos')
    else:
        print('❌ No se detectó como tabla de cartera')
else:
    print('❌ Error en extracción')
