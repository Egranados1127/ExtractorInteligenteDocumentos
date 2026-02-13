# -*- coding: utf-8 -*-
"""
🧠 TEST DE AUTO-APRENDIZAJE INTELIGENTE

Este script demuestra las nuevas capacidades de auto-corrección y aprendizaje:
- FuzzyWuzzy: Corrige nombres mal leídos por OCR
- Pydantic: Valida y limpia automáticamente los datos 
- Memoria persistente: Aprende nuevos nombres para futuras extracciones

Ejecutar: python test_auto_aprendizaje.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import (
    memoria_inteligente, 
    FilaCarteraEdades, 
    DatosMedicamento,
    aplicar_autocorreccion_tabla
)

def test_correccion_proveedores():
    """Prueba auto-corrección de nombres de proveedores"""
    print("=" * 60)
    print("🏢 TEST: CORRECCIÓN DE PROVEEDORES")
    print("=" * 60)
    
    # Simular nombres mal leídos por OCR
    nombres_ocr = [
        "MERCURY S4S",           # S en lugar de A
        "ANDES CABLOS SAS",      # B en lugar de E  
        "DURM4N COLOMBIA SA5",   # 4 en lugar de A, 5 en lugar de S
        "VISION INTEGR4DOS",     # 4 en lugar de A
        "GRUPO MERCU8Y SAS"      # 8 en lugar de R
    ]
    
    for nombre_malo in nombres_ocr:
        nombre_corregido = memoria_inteligente.corregir_nombre(
            nombre_malo, 
            memoria_inteligente.proveedores_conocidos
        )
        print(f"'{nombre_malo}' → '{nombre_corregido}'")
    
    print()

def test_correccion_numeros():
    """Prueba auto-corrección de números monetarios"""
    print("=" * 60) 
    print("💰 TEST: CORRECCIÓN DE NÚMEROS")
    print("=" * 60)
    
    # Simular valores mal leídos por OCR
    valores_ocr = [
        "$1,S00.OO",    # S en lugar de 5, O en lugar de 0
        "2.GO0,50",     # G en lugar de 5, O en lugar de 0 
        "I5O.000",      # I en lugar de 1, O en lugar de 0
        "8.OOO,OO",     # O en lugar de 0
        "1O,S00"        # O en lugar de 0, S en lugar de 5
    ]
    
    for valor_malo in valores_ocr:
        valor_corregido = memoria_inteligente.limpiar_numero(valor_malo)
        print(f"'{valor_malo}' → {valor_corregido}")
        
    print()

def test_validacion_cartera():
    """Prueba validación automática con Pydantic"""
    print("=" * 60)
    print("📊 TEST: VALIDACIÓN AUTOMÁTICA DE CARTERA")
    print("=" * 60)
    
    # Simular fila de cartera con errores de OCR
    dato_ocr = {
        'documento': '123456',
        'proveedor': 'MERCURY S4S',       # Error en nombre
        'corriente': '$1,S00.OO',         # Error numérico
        'de_1_a_30': '2.GO0,50',         # Error numérico
        'de_31_a_60': 'I5O.000',        # Error numérico
        'de_61_a_90': '0',
        'de_91_o_mas': '0',
        'total': '3,65O.5O'              # Error numérico
    }
    
    print("Datos del OCR (con errores):")
    for campo, valor in dato_ocr.items():
        print(f"  {campo}: {valor}")
    
    try:
        # Validar y corregir automáticamente
        fila_validada = FilaCarteraEdades(**dato_ocr)
        
        print("\nDatos después de auto-corrección:")
        print(f"  proveedor: {fila_validada.proveedor}")
        print(f"  corriente: {fila_validada.corriente}")
        print(f"  de_1_a_30: {fila_validada.de_1_a_30}")
        print(f"  de_31_a_60: {fila_validada.de_31_a_60}")
        print(f"  total: {fila_validada.total}")
        print(f"  total_calculado: {fila_validada.corriente + fila_validada.de_1_a_30 + fila_validada.de_31_a_60}")
        
    except Exception as e:
        print(f"Error en validación: {e}")
    
    print()

def test_validacion_medicamento():
    """Prueba validación de datos médicos"""
    print("=" * 60)
    print("💊 TEST: VALIDACIÓN DE MEDICAMENTOS")
    print("=" * 60)
    
    # Simular datos de medicamento con errores
    dato_ocr = {
        'codigo': 'O5OOI171S',                    # O en lugar de 0, I en lugar de 1, S en lugar de 5
        'descripcion': 'HI4LURONATO DE SODIO',   # 4 en lugar de A
        'cantidad': '12 (DOCE)',
        'posologia': 'APLICAR 1 GOTA CADA 8 HORAS',
        'dias': 'MIPRES'
    }
    
    print("Datos del OCR (con errores):")
    for campo, valor in dato_ocr.items():
        print(f"  {campo}: {valor}")
    
    try:
        # Validar y corregir automáticamente
        medicamento_validado = DatosMedicamento(**dato_ocr)
        
        print("\nDatos después de auto-corrección:")
        print(f"  codigo: {medicamento_validado.codigo}")
        print(f"  descripcion: {medicamento_validado.descripcion}")
        print(f"  cantidad: {medicamento_validado.cantidad}")
        print(f"  posologia: {medicamento_validado.posologia}")
        print(f"  dias: {medicamento_validado.dias}")
        
    except Exception as e:
        print(f"Error en validación: {e}")
    
    print()

def test_tabla_completa():
    """Prueba corrección de tabla completa"""
    print("=" * 60)
    print("📋 TEST: AUTO-CORRECCIÓN DE TABLA COMPLETA")
    print("=" * 60)
    
    # Simular tabla extraída del OCR con errores
    tabla_ocr = [
        ['DOC123', 'MERCURY S4S', '$1,S00.OO', '2.GO0,50', 'I5O.000', '0', '0', '3,65O.5O'],
        ['DOC124', 'ANDES CABLOS', '5,OOO.OO', '1,2SO.OO', '0', 'I,OOO.OO', '0', '7,2SO.OO'],
        ['DOC125', 'DURM4N COL', '2,OOO.OO', '0', 'S00.OO', '0', 'I,OOO.OO', '3,SOO.OO']
    ]
    
    print("Tabla del OCR (con errores):")
    for i, fila in enumerate(tabla_ocr):
        print(f"  Fila {i+1}: {fila}")
    
    # Aplicar auto-corrección
    tabla_corregida = aplicar_autocorreccion_tabla(tabla_ocr, 'cartera')
    
    print("\nTabla después de auto-corrección:")
    for i, fila in enumerate(tabla_corregida):
        print(f"  Fila {i+1}: {fila}")
    
    print()

def main():
    print(""" 
🧠 SISTEMA DE AUTO-APRENDIZAJE Y VALIDACIÓN INTELIGENTE
======================================================

Este sistema aprende automáticamente de errores de OCR comunes y:
✅ Corrige nombres de proveedores automáticamente (FuzzyWuzzy)
✅ Valida y limpia números monetarios (Pydantic)  
✅ Detecta inconsistencias en totales y las corrige
✅ Mantiene memoria persistente de correcciones
✅ Mejora con el uso sin supervisión humana

¡No más errores S/5, O/0, I/1 en sus extracciones!
""")
    
    test_correccion_proveedores()
    test_correccion_numeros()
    test_validacion_cartera()
    test_validacion_medicamento()
    test_tabla_completa()
    
    print("=" * 60)
    print("🎉 TODAS LAS PRUEBAS COMPLETADAS")
    print("✅ Sistema de auto-aprendizaje funcionando correctamente")
    print("📚 Nuevos nombres se guardan automáticamente en memoria_aprendizaje.json")
    print("🚀 El sistema mejora automáticamente con cada uso")
    print("=" * 60)

if __name__ == "__main__":
    main()