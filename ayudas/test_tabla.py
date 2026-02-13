import sys
from app import extraer_datos
from PIL import Image

img_path = r'C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-31 at 12.53.22 PM.jpeg'

resultado = extraer_datos(Image.open(img_path), 'WhatsApp Image.jpeg')

print(f'Tipo: {resultado.get("_tipo", "normal")}')
print(f'Filas detectadas: {len(resultado.get("_filas", []))}')
print('\nFILAS COMPLETAS:')
print("=" * 80)
    print("=" * 80)
    print()
    
    # Hacer OCR
    print("📄 Ejecutando OCR...")
    imagen = Image.open(ruta_imagen)
    texto = pytesseract.image_to_string(imagen, lang='spa', config='--psm 3 --dpi 200')
    
    print("\n📋 TEXTO OCR COMPLETO:")
    print("-" * 80)
    print(texto)
    print("-" * 80)
    print()
    
    # Extraer tablas
    print("🔍 Extrayendo tablas...")
    tablas = extraer_tablas(texto)
    
    if not tablas:
        print("❌ No se detectaron tablas")
        return
    
    print(f"✅ Se detectaron {len(tablas)} tabla(s)\n")
    
    # Mostrar cada tabla
    for i, tabla in enumerate(tablas, 1):
        print(f"\n{'=' * 80}")
        print(f"TABLA {i}: {tabla['nombre']}")
        print(f"{'=' * 80}")
        
        headers = tabla['encabezados']
        data = tabla['data']
        
        print(f"\n📌 Encabezados ({len(headers)} columnas):")
        for idx, h in enumerate(headers, 1):
            print(f"  {idx}. {repr(h)}")
        
        print(f"\n📊 Datos ({len(data)} filas):")
        for idx, fila in enumerate(data, 1):
            print(f"\n  Fila {idx}:")
            for col_idx, celda in enumerate(fila):
                print(f"    {headers[col_idx]}: {repr(celda)}")
        
        print()

if __name__ == "__main__":
    # Ejemplo de uso
    # Cambia esta ruta por tu imagen con tabla
    ruta = input("📂 Ingresa la ruta de la imagen con tabla (o presiona Enter para ejemplo): ").strip()
    
    if not ruta:
        # Ruta de ejemplo
        ruta = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\tabla.jpg"
        print(f"Usando ejemplo: {ruta}")
    
    # Limpiar comillas si las pegó
    ruta = ruta.strip('"').strip("'")
    
    if Path(ruta).exists():
        test_tabla_desde_imagen(ruta)
    else:
        print(f"❌ No se encontró el archivo: {ruta}")
        print("\nTip: Arrastra el archivo a la consola para copiar la ruta automáticamente")
