from PIL import Image
from paddleocr import PaddleOCR
import numpy as np

print('DEBUG: Analisis completo de PaddleOCR')
print('=' * 80)

img_path = r'C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-08 at 8.09.55 PM.jpeg'
imagen = Image.open(img_path)

# Inicializar PaddleOCR (versión 2.7.x)
ocr = PaddleOCR(use_angle_cls=True, lang='es', show_log=False)

# Convertir a numpy
img_array = np.array(imagen)

# Ejecutar OCR usando API 2.7.x
result = ocr.ocr(img_array, cls=True)

print(f'\nTotal de elementos detectados: {len(result[0])}')
print('\n' + '=' * 80)
print('TODOS LOS ELEMENTOS (primeros 50):')
print('=' * 80)

# Mostrar primeros 50 elementos con coordenadas
for i, line in enumerate(result[0][:50]):
    bbox = line[0]
    texto = line[1][0]
    confianza = line[1][1]
    
    # Calcular centro
    y_centro = sum([punto[1] for punto in bbox]) / 4
    x_centro = sum([punto[0] for punto in bbox]) / 4
    
    print(f'{i+1:3d}. Y={y_centro:6.1f} X={x_centro:6.1f} Conf={confianza:.2f} "{texto}"')

print('\n' + '=' * 80)
print('AGRUPACION POR FILAS (tolerancia Y=15):')
print('=' * 80)

# Extraer elementos con coordenadas
elementos = []
for line in result[0]:
    bbox = line[0]
    texto = line[1][0]
    confianza = line[1][1]
    
    y_centro = sum([punto[1] for punto in bbox]) / 4
    x_centro = sum([punto[0] for punto in bbox]) / 4
    
    elementos.append({
        'texto': texto,
        'x': x_centro,
        'y': y_centro,
        'confianza': confianza
    })

# Agrupar por filas
tolerancia_y = 15
filas_agrupadas = []
elementos_usados = set()

elementos_ordenados = sorted(elementos, key=lambda e: e['y'])

for elem in elementos_ordenados:
    if id(elem) in elementos_usados:
        continue
        
    fila_actual = []
    for otro_elem in elementos_ordenados:
        if id(otro_elem) in elementos_usados:
            continue
        if abs(otro_elem['y'] - elem['y']) <= tolerancia_y:
            fila_actual.append(otro_elem)
            elementos_usados.add(id(otro_elem))
    
    if fila_actual:
        fila_ordenada = sorted(fila_actual, key=lambda e: e['x'])
        filas_agrupadas.append(fila_ordenada)

print(f'\nTotal filas agrupadas: {len(filas_agrupadas)}')
print('\nPrimeras 15 filas con su numero de columnas:')
for i, fila in enumerate(filas_agrupadas[:15], 1):
    textos = [elem['texto'][:20] for elem in fila]
    print(f'{i:2d}. [{len(fila)}cols] {" | ".join(textos)}')

print('\n' + '=' * 80)
print('FILAS CON EXACTAMENTE 8 COLUMNAS:')
print('=' * 80)

for i, fila in enumerate(filas_agrupadas):
    if len(fila) == 8:
        textos = [elem['texto'] for elem in fila]
        print(f'\nFila con 8 cols: {textos}')
