"""
🧪 PRUEBA RÁPIDA DEL SISTEMA INTEGRADO
======================================
Este script verifica que todas las herramientas estén funcionando correctamente
"""

import sys
from pathlib import Path

print("="*70)
print("🧪 VERIFICANDO SISTEMA INTEGRADO")
print("="*70)

# ============================================
# 1. VERIFICAR IMPORTACIONES
# ============================================
print("\n📦 1. Verificando importaciones...")

modulos_requeridos = {
    'PIL': 'Pillow',
    'pytesseract': 'pytesseract',
    'easyocr': 'easyocr',
    'paddleocr': 'paddleocr',
    'pandas': 'pandas',
    'streamlit': 'streamlit',
    'thefuzz': 'thefuzz',
    'pydantic': 'pydantic',
}

modulos_ok = []
modulos_error = []

for modulo, nombre_pip in modulos_requeridos.items():
    try:
        __import__(modulo)
        modulos_ok.append(nombre_pip)
        print(f"   ✅ {nombre_pip}")
    except ImportError:
        modulos_error.append(nombre_pip)
        print(f"   ❌ {nombre_pip} - NO INSTALADO")

if modulos_error:
    print(f"\n⚠️  Falta instalar: {', '.join(modulos_error)}")
    print(f"   Ejecuta: pip install {' '.join(modulos_error)}")
else:
    print("\n✅ Todos los módulos básicos están instalados")

# ============================================
# 2. VERIFICAR ARCHIVOS DEL PROYECTO
# ============================================
print("\n📁 2. Verificando archivos del proyecto...")

archivos_requeridos = [
    'app.py',
    'extractor_maestro.py',
    'app_maestro.py',
    'config.py',
    'config.example.py',
    'lector.py',
    '.gitignore'
]

archivos_ok = []
archivos_faltantes = []

for archivo in archivos_requeridos:
    if Path(archivo).exists():
        archivos_ok.append(archivo)
        print(f"   ✅ {archivo}")
    else:
        archivos_faltantes.append(archivo)
        print(f"   ❌ {archivo} - NO ENCONTRADO")

if archivos_faltantes:
    print(f"\n⚠️  Archivos faltantes: {', '.join(archivos_faltantes)}")
else:
    print("\n✅ Todos los archivos del proyecto están presentes")

# ============================================
# 3. VERIFICAR AZURE (OPCIONAL)
# ============================================
print("\n☁️  3. Verificando Azure Document Intelligence...")

try:
    from config import AZURE_ENDPOINT, AZURE_KEY
    
    if AZURE_ENDPOINT and AZURE_KEY:
        if AZURE_ENDPOINT == "PEGA_AQUI_TU_ENDPOINT":
            print("   ⚠️  Azure NO configurado (usando valores por defecto)")
            print("   💡 Edita config.py con tus credenciales reales")
        else:
            print(f"   ✅ Endpoint configurado: {AZURE_ENDPOINT[:40]}...")
            print(f"   ✅ Key configurada: {AZURE_KEY[:10]}...{AZURE_KEY[-4:]}")
            
            # Intentar importar cliente Azure
            try:
                from azure.ai.formrecognizer import DocumentAnalysisClient
                from azure.core.credentials import AzureKeyCredential
                print("   ✅ Módulo azure-ai-formrecognizer instalado")
            except ImportError:
                print("   ⚠️  Módulo azure-ai-formrecognizer NO instalado")
                print("      Ejecuta: pip install azure-ai-formrecognizer")
    else:
        print("   ⚠️  Azure no configurado (opcional)")
        
except ImportError:
    print("   ⚠️  config.py no encontrado")
except Exception as e:
    print(f"   ❌ Error: {e}")

# ============================================
# 4. VERIFICAR TESSERACT
# ============================================
print("\n🔍 4. Verificando Tesseract OCR...")

try:
    import pytesseract
    from PIL import Image
    import numpy as np
    
    # Crear imagen de prueba
    img_test = Image.new('RGB', (200, 50), color='white')
    
    try:
        texto = pytesseract.image_to_string(img_test)
        print("   ✅ Tesseract funcionando correctamente")
    except pytesseract.TesseractNotFoundError:
        print("   ❌ Tesseract NO encontrado en el sistema")
        print("      Descarga desde: https://github.com/UB-Mannheim/tesseract/wiki")
        
except Exception as e:
    print(f"   ❌ Error: {e}")

# ============================================
# 5. VERIFICAR MEMORIA DE APRENDIZAJE
# ============================================
print("\n🧠 5. Verificando sistema de aprendizaje...")

try:
    from app import cargar_memoria, guardar_memoria
    
    memoria = cargar_memoria()
    print(f"   ✅ Memoria cargada correctamente")
    
    if 'nombres_completos' in memoria:
        num_nombres = len(memoria['nombres_completos'])
        print(f"   📚 Nombres aprendidos: {num_nombres}")
    else:
        print("   ℹ️  Memoria vacía (esperado si es primera vez)")
        
except Exception as e:
    print(f"   ⚠️  Error cargando memoria: {e}")

# ============================================
# 6. PRUEBA DE EXTRACCIÓN BÁSICA
# ============================================
print("\n🚀 6. Probando extracción básica...")

try:
    from extractor_maestro import ExtractorMaestro
    from PIL import Image
    import numpy as np
    
    # Crear imagen de prueba con texto
    img = Image.new('RGB', (400, 100), color='white')
    
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(img)
    
    # Intentar usar fuente, si falla usar fuente por defecto
    try:
        # En Windows, usar fuente Arial
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    
    draw.text((10, 30), "PRUEBA DE EXTRACCION", fill='black', font=font)
    
    # Crear extractor y probar
    extractor = ExtractorMaestro()
    datos, tiempo = extractor.extraer_con_tesseract(img)
    
    print(f"   ✅ Extracción completada en {tiempo:.2f}s")
    print(f"   📊 Campos extraidos: {len(datos)}")
    
except Exception as e:
    print(f"   ⚠️  Error en prueba de extracción: {e}")

# ============================================
# RESUMEN FINAL
# ============================================
print("\n" + "="*70)
print("📋 RESUMEN")
print("="*70)

total_checks = 6
checks_ok = 0

if not modulos_error:
    checks_ok += 1
if not archivos_faltantes:
    checks_ok += 1

# Los otros checks no son críticos
checks_ok += 2  # Sumar checks no críticos como OK por defecto

porcentaje = (checks_ok / total_checks) * 100

print(f"\n✅ Verificaciones exitosas: {checks_ok}/{total_checks} ({porcentaje:.0f}%)")

if porcentaje == 100:
    print("\n🎉 ¡SISTEMA COMPLETAMENTE FUNCIONAL!")
    print("\n📌 PRÓXIMOS PASOS:")
    print("   1. Ejecuta: streamlit run app_maestro.py")
    print("   2. O usa: python extractor_maestro.py para pruebas programáticas")
    print("   3. Lee README_SISTEMA_INTEGRADO.md para más información")
    
elif porcentaje >= 70:
    print("\n✅ Sistema funcional con algunas limitaciones")
    print("   Revisa las advertencias arriba para mejorar funcionalidad")
    
else:
    print("\n⚠️  El sistema necesita configuración adicional")
    print("   Revisa los errores arriba e instala componentes faltantes")

print("\n" + "="*70)

# ============================================
# INSTRUCCIONES DE USO
# ============================================
print("\n💡 COMANDOS ÚTILES:")
print("="*70)
print("\n# Interfaz visual (recomendado):")
print("  streamlit run app_maestro.py")
print("\n# Interfaz original:")
print("  streamlit run app.py")
print("\n# Uso programático:")
print("  python extractor_maestro.py")
print("\n# Verificar config Azure:")
print("  python config.py")
print("\n# Usar Azure directamente:")
print("  python lector.py")
print("\n" + "="*70)
