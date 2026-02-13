# -*- coding: utf-8 -*-
"""
Script de instalación automática del modelo de español para spaCy
Ejecutar este script después de instalar los requirements
"""

import subprocess
import sys

def instalar_modelo_espanol():
    """Instala el modelo de español pequeño de spaCy"""
    print("=" * 60)
    print("🚀 INSTALADOR DEL MODELO DE ESPAÑOL PARA SPACY")
    print("=" * 60)
    print()
    
    try:
        # Verificar si spaCy está instalado
        print("📦 Verificando instalación de spaCy...")
        import spacy
        print(f"✅ spaCy {spacy.__version__} encontrado")
        print()
        
    except ImportError:
        print("❌ spaCy no está instalado")
        print("💡 Ejecuta primero: pip install -r requirements_app.txt")
        return False
    
    try:
        # Intentar cargar el modelo
        print("🔍 Verificando modelo de español...")
        nlp = spacy.load("es_core_news_sm")
        print("✅ El modelo 'es_core_news_sm' ya está instalado")
        print()
        print("🎉 ¡Todo listo! Puedes usar la extracción con IA")
        return True
        
    except OSError:
        # El modelo no está instalado, proceder a instalarlo
        print("📥 Modelo no encontrado. Procediendo a instalar...")
        print()
        
        try:
            # Descargar el modelo
            print("⏳ Descargando modelo es_core_news_sm...")
            print("   (Esto puede tomar unos minutos)")
            print()
            
            resultado = subprocess.run(
                [sys.executable, "-m", "spacy", "download", "es_core_news_sm"],
                capture_output=True,
                text=True
            )
            
            if resultado.returncode == 0:
                print("✅ Modelo instalado exitosamente!")
                print()
                
                # Verificar la instalación
                print("🧪 Verificando instalación...")
                nlp = spacy.load("es_core_news_sm")
                print("✅ Verificación exitosa!")
                print()
                print("=" * 60)
                print("🎉 ¡INSTALACIÓN COMPLETADA CON ÉXITO!")
                print("=" * 60)
                print()
                print("Ahora puedes ejecutar la aplicación:")
                print("  streamlit run app.py")
                print()
                return True
            else:
                print("❌ Error durante la instalación:")
                print(resultado.stderr)
                return False
                
        except Exception as e:
            print(f"❌ Error inesperado: {str(e)}")
            print()
            print("💡 Intenta instalarlo manualmente:")
            print("   python -m spacy download es_core_news_sm")
            return False

if __name__ == "__main__":
    exito = instalar_modelo_espanol()
    
    if exito:
        print()
        input("Presiona Enter para salir...")
    else:
        print()
        print("⚠️ La instalación no se completó correctamente")
        print("Revisa los mensajes de error arriba")
        input("Presiona Enter para salir...")
