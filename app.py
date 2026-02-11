# -*- coding: utf-8 -*-
import streamlit as st
import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes
import pandas as pd
import re
import io
import os

# Configurar Tesseract con variables de entorno
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ===============================
# FUNCIONES DE NORMALIZACION
# ===============================
def normalizar_texto(texto):
    """Normaliza el texto para facilitar busqueda"""
    if not texto:
        return ""
    texto = re.sub(r'\s+', ' ', str(texto)).strip()
    texto = texto.replace('\n', ' ').replace('\r', '')
    return texto

def buscar(patron, texto, grupo=1):
    """Busca un patron regex en el texto"""
    if not texto:
        return ""
    match = re.search(patron, texto, re.IGNORECASE | re.DOTALL)
    return match.group(grupo).strip() if match else ""

# ===============================
# FUNCIONES OCR
# ===============================
def ocr_pdf_bytes(pdf_bytes, max_paginas=2, dpi=100):
    """Extrae texto de un PDF usando OCR"""
    try:
        imagenes = convert_from_bytes(
            pdf_bytes,
            dpi=dpi,
            first_page=1,
            last_page=min(max_paginas, 5)
        )
        
        texto_completo = []
        for i, img in enumerate(imagenes, 1):
            texto = pytesseract.image_to_string(img, lang='spa', config='--psm 1')
            texto_completo.append(texto)
        
        return "\n".join(texto_completo)
    except Exception as e:
        raise Exception(f"Error en OCR de PDF: {str(e)}")

def ocr_imagen(imagen):
    """Extrae texto de una imagen usando OCR"""
    try:
        if max(imagen.size) > 4000:
            ratio = 4000 / max(imagen.size)
            nuevo_tam = tuple(int(dim * ratio) for dim in imagen.size)
            imagen = imagen.resize(nuevo_tam, Image.Resampling.LANCZOS)
        
        return pytesseract.image_to_string(imagen, lang='spa', config='--psm 1')
    except Exception as e:
        raise Exception(f"Error en OCR de imagen: {str(e)}")

# ===============================
# FUNCION DE EXTRACCION GENERICA
# ===============================
def extraer_datos(texto, nombre_archivo=""):
    """Extrae informacion clave de cualquier tipo de documento"""
    
    texto_norm = normalizar_texto(texto)
    
    # Diccionario para almacenar los datos extraidos
    datos = {'_archivo': nombre_archivo}
    
    # ===== FECHAS =====
    fechas_encontradas = re.findall(
        r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{1,2}\s+de\s+\w+\s+de\s+\d{4}|\d{4}[/-]\d{2}[/-]\d{2}',
        texto_norm
    )
    for i, fecha in enumerate(fechas_encontradas[:5], 1):
        datos[f'Fecha_{i}'] = fecha
    
    # ===== NUMEROS DE DOCUMENTO =====
    # Resoluciones, radicados, licencias, etc.
    num_resolucion = buscar(
        r'(?:RESOLUCI[OÓ]N|RESOLUCION)\s*(?:No\.?|N[UÚ]MERO|NUM)?\s*[:.]?\s*([A-Z0-9-]{3,20})',
        texto_norm
    )
    if num_resolucion:
        datos['Numero_Resolucion'] = num_resolucion
    
    radicado = buscar(
        r'(?:RADICAD[OA]|RADICACI[OÓ]N)\s*(?:No\.?|N[UÚ]MERO)?[:.]?\s*([A-Z0-9-]{5,25})',
        texto_norm
    )
    if radicado:
        datos['Radicado'] = radicado
    
    # Cualquier numero de documento generico
    num_docs = re.findall(
        r'(?:NO\.|N[UÚ]MERO|NUM\.?|#)\s*[:.]?\s*([A-Z0-9-]{3,20})',
        texto_norm
    )
    for i, num in enumerate(num_docs[:3], 1):
        if num not in datos.values():
            datos[f'Numero_Documento_{i}'] = num
    
    # ===== IDENTIFICACIONES =====
    # Cedulas
    cedulas = re.findall(r'(?:C\.?C\.?|CEDULA|CED\.?)\s*(?:No\.?)?[:.]?\s*([0-9.]{7,15})', texto_norm)
    for i, cc in enumerate(cedulas[:3], 1):
        datos[f'Cedula_{i}'] = cc.replace('.', '')
    
    # NITs
    nits = re.findall(r'NIT\s*(?:No\.?)?[:.]?\s*([0-9.-]{9,15})', texto_norm)
    for i, nit in enumerate(nits[:2], 1):
        datos[f'NIT_{i}'] = nit
    
    # ===== NOMBRES Y PERSONAS =====
    # Buscar nombres propios (2-4 palabras capitalizadas)
    nombres = re.findall(
        r'\b([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+){1,3})\b',
        texto
    )
    # Filtrar nombres muy comunes que no son personas
    palabras_excluir = {'El', 'La', 'Los', 'Las', 'De', 'Del', 'En', 'Por', 'Para', 'Con', 'Sin'}
    nombres_unicos = []
    for nombre in nombres:
        if nombre not in nombres_unicos and nombre not in palabras_excluir:
            nombres_unicos.append(nombre)
    
    for i, nombre in enumerate(nombres_unicos[:5], 1):
        datos[f'Nombre_{i}'] = nombre
    
    # ===== DIRECCIONES =====
    direcciones = re.findall(
        r'(?:DIRECCI[OÓ]N|DIR\.?|UBICAD[OA])\s*[:.]?\s*([A-Z0-9ÁÉÍÓÚÑ#\-\s.,]{10,80})',
        texto_norm
    )
    for i, dir in enumerate(direcciones[:2], 1):
        datos[f'Direccion_{i}'] = dir.strip()
    
    # Direcciones con formato de calle/carrera
    dirs_formato = re.findall(
        r'(?:CL|CLL|CALLE|KR|KRA|CARRERA|DG|DIAGONAL|TV|TRANSVERSAL)\.?\s+[0-9A-Z#\-\s]{5,40}',
        texto_norm
    )
    for i, dir in enumerate(dirs_formato[:2], 1):
        if dir.strip() not in datos.values():
            datos[f'Direccion_Formato_{i}'] = dir.strip()
    
    # ===== TELEFONOS =====
    telefonos = re.findall(
        r'(?:TEL[EÉ]FONO|TEL\.?|CELULAR|CEL\.?|M[OÓ]VIL)\s*[:.]?\s*([0-9\-\(\)\s]{7,15})',
        texto_norm
    )
    for i, tel in enumerate(telefonos[:3], 1):
        datos[f'Telefono_{i}'] = tel.strip()
    
    # ===== EMAILS =====
    emails = re.findall(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        texto
    )
    for i, email in enumerate(emails[:3], 1):
        datos[f'Email_{i}'] = email
    
    # ===== VALORES MONETARIOS =====
    valores = re.findall(
        r'(?:\$|COP|USD|EUR)\s*([0-9.,]+)|([0-9.,]+)\s*(?:PESOS|D[OÓ]LARES)',
        texto_norm
    )
    for i, valor in enumerate(valores[:3], 1):
        val = valor[0] if valor[0] else valor[1]
        if val:
            datos[f'Valor_Monetario_{i}'] = val
    
    # ===== CANTIDADES Y MEDIDAS =====
    # Areas, metros cuadrados
    areas = re.findall(
        r'([0-9.,]+)\s*(?:M2|M²|METROS?\s+CUADRADOS?|MTS2)',
        texto_norm
    )
    for i, area in enumerate(areas[:3], 1):
        datos[f'Area_M2_{i}'] = area
    
    # Otras cantidades con unidades
    cantidades = re.findall(
        r'([0-9.,]+)\s*(KG|KILOS?|LITROS?|TONELADAS?|UNIDADES?|UND)',
        texto_norm
    )
    for i, (cant, unidad) in enumerate(cantidades[:3], 1):
        datos[f'Cantidad_{i}'] = f"{cant} {unidad}"
    
    # ===== CODIGOS Y REFERENCIAS =====
    # Codigos alfanumericos
    codigos = re.findall(
        r'(?:C[OÓ]DIGO|COD\.?|REF\.?|REFERENCIA)\s*[:.]?\s*([A-Z0-9-]{5,20})',
        texto_norm
    )
    for i, cod in enumerate(codigos[:3], 1):
        datos[f'Codigo_{i}'] = cod
    
    # ===== LUGARES Y CIUDADES =====
    ciudades = re.findall(
        r'(?:MUNICIPIO|CIUDAD)\s*[:.]?\s*([A-ZÁÉÍÓÚÑ\s]{3,30})',
        texto_norm
    )
    for i, ciudad in enumerate(ciudades[:2], 1):
        datos[f'Ciudad_Municipio_{i}'] = ciudad.strip()
    
    # ===== PALABRAS CLAVE Y DECISIONES =====
    # Buscar decisiones o estados
    if re.search(r'\b(?:APROBA[DR]O|APRUEBA|ACEPTA[DR]O|AUTORIZA[DR]O|CONCEDE|OTORGA)\b', texto_norm, re.IGNORECASE):
        datos['Estado_Decision'] = 'APROBADO'
    elif re.search(r'\b(?:NEGA[DR]O|NIEGA|RECHAZA[DR]O|INADMITE|IMPROCEDENTE)\b', texto_norm, re.IGNORECASE):
        datos['Estado_Decision'] = 'NEGADO'
    elif re.search(r'\b(?:PENDIENTE|EN\s+PROCESO|EN\s+TR[AÁ]MITE)\b', texto_norm, re.IGNORECASE):
        datos['Estado_Decision'] = 'PENDIENTE'
    
    # Eliminar entradas vacias
    datos_limpios = {k: v for k, v in datos.items() if v}
    
    return datos_limpios

# ===============================
# ===============================
# APLICACION STREAMLIT
# ===============================
# ===============================

def main():
    st.set_page_config(
        page_title="Extractor Inteligente | V&G",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # CSS PROFESIONAL
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }
        
        .main-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2.5rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
            text-align: center;
        }
        
        .main-header h1 {
            color: white;
            font-size: 2.8rem;
            font-weight: 700; 
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        
        .main-header p {
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.2rem;
            margin-top: 0.5rem;
            font-weight: 300;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 1rem 3rem;
            font-size: 1.1rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
            width: 100%;
        }
        
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.6);
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        }
        
        .metric-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 2rem 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
            border-color: #667eea;
        }
        
        .metric-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .metric-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: #667eea;
            margin: 0.5rem 0;
        }
        
        .metric-label {
            color: #4a5568;
            font-size: 0.9rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .section-header {
            background: linear-gradient(90deg, #667eea 0%, transparent 100%);
            padding: 1rem 1.5rem;
            border-radius: 10px;
            color: white;
            font-weight: 600;
            font-size: 1.4rem;
            margin: 2rem 0 1rem 0;
            box-shadow: 0 4px 10px rgba(102, 126, 234, 0.2);
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background-color: #f7fafc;
            padding: 0.8rem;
            border-radius: 12px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 10px;
            padding: 1rem 2rem;
            font-weight: 600;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            box-shadow: 0 4px 10px rgba(102, 126, 234, 0.3);
        }
        
        .stFileUploader {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 2rem;
            border-radius: 15px;
            border: 3px dashed #667eea;
        }
        
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #f7fafc 0%, #edf2f7 100%);
        }
        
        .stDownloadButton > button {
            background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.8rem 2rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(72, 187, 120, 0.3);
        }
        
        .stDownloadButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(72, 187, 120, 0.4);
        }
        
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 700;
            color: #667eea;
        }
        
        hr {
            margin: 2rem 0;
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent 0%, #667eea 50%, transparent 100%);
        }
        </style>
    """, unsafe_allow_html=True)
    
    # HEADER PRINCIPAL
    st.markdown("""
        <div class="main-header">
            <h1>&#128196; Extractor Inteligente de Documentos</h1>
            <p>Sistema de Analisis Automatizado con Tecnologia OCR</p>
        </div>
    """, unsafe_allow_html=True)
    
    # SIDEBAR
    with st.sidebar:
        st.markdown("### &#9881; Panel de Control")
        st.markdown("")
        
        st.markdown("#### &#128295; Configuracion OCR")
        max_paginas = st.slider(
            "Paginas a procesar",
            min_value=1,
            max_value=5,
            value=2,
            help="Mas paginas = mayor precision pero mas lento"
        )
        
        dpi = st.selectbox(
            "Calidad de escaneo",
            options=[75, 100, 150, 200, 300],
            index=1,
            format_func=lambda x: f"{x} DPI - {'Rapido' if x < 100 else 'Balanceado' if x <= 150 else 'Alta calidad'}",
            help="Mayor DPI = mejor calidad"
        )
        
        st.markdown("---")
        
        st.markdown("#### &#128161; Consejos Pro")
        st.info("Documentos claros = mejor precision\\n\\nPrimera pagina tiene mas info\\n\\nDPI 100-150 es optimo\\n\\nSoporta: PDF, PNG, JPG, TIFF")
        
        st.markdown("---")
        
        if 'texto' in st.session_state:
            st.markdown("#### &#128202; Estadisticas")
            texto_len = len(st.session_state.get('texto', ''))
            st.metric("Caracteres extraidos", f"{texto_len:,}")
        
        st.markdown("---")
        st.caption("Extractor Inteligente v3.0 | Powered by Tesseract OCR")
    
    # PASO 1: CARGAR DOCUMENTO
    st.markdown('<div class="section-header">&#128193; PASO 1: Cargar Documento</div>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Arrastra tu archivo aqui o haz clic para seleccionar",
        type=['pdf', 'png', 'jpg', 'jpeg', 'tiff'],
        help="Formatos soportados: PDF, PNG, JPG, JPEG, TIFF"
    )
    
    if uploaded_file:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-icon">&#128196;</div>
                    <div class="metric-label">Nombre del Archivo</div>
                    <div class="metric-value" style="font-size: 1.1rem;">{uploaded_file.name[:25]}{'...' if len(uploaded_file.name) > 25 else ''}</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-icon">&#128194;</div>
                    <div class="metric-label">Tipo de Archivo</div>
                    <div class="metric-value">{uploaded_file.type.split('/')[-1].upper()}</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            size_kb = uploaded_file.size / 1024
            size_display = f"{size_kb:.1f} KB" if size_kb < 1024 else f"{size_kb/1024:.1f} MB"
            st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-icon">&#128190;</div>
                    <div class="metric-label">Tamaño</div>
                    <div class="metric-value">{size_display}</div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("&#128269; PROCESAR DOCUMENTO", type="primary", use_container_width=True):
                progress_bar = st.progress(0)
                status = st.empty()
                
                try:
                    status.info("&#128193; Cargando archivo...")
                    progress_bar.progress(25)
                    
                    file_ext = uploaded_file.name.split('.')[-1].lower()
                    
                    status.info("&#128270; Ejecutando OCR... Esto puede tomar unos segundos")
                    progress_bar.progress(50)
                    
                    if file_ext == 'pdf':
                        pdf_bytes = uploaded_file.read()
                        texto = ocr_pdf_bytes(pdf_bytes, max_paginas, dpi)
                    else:
                        imagen = Image.open(uploaded_file)
                        texto = ocr_imagen(imagen)
                    
                    progress_bar.progress(75)
                    status.info("&#128202; Extrayendo informacion...")
                    
                    st.session_state['texto'] = texto
                    st.session_state['archivo'] = uploaded_file.name
                    
                    progress_bar.progress(100)
                    status.empty()
                    st.success("&#9989; Documento procesado exitosamente!")
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"&#10060; Error al procesar: {str(e)}")
                    st.info("&#128161; Verifica que Tesseract OCR este instalado")
    
    # PASO 2: RESULTADOS
    if 'texto' in st.session_state:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<div class="section-header">&#128202; PASO 2: Resultados del Analisis</div>', unsafe_allow_html=True)
        
        datos = extraer_datos(st.session_state['texto'], st.session_state['archivo'])
        
        col1, col2, col3, col4 = st.columns(4)
        
        # Contar campos por categoria
        total_campos = len(datos) - 1  # -1 por el _archivo
        fechas = sum(1 for k in datos.keys() if 'Fecha' in k)
        identificaciones = sum(1 for k in datos.keys() if 'Cedula' in k or 'NIT' in k)
        nombres = sum(1 for k in datos.keys() if 'Nombre' in k)
        
        with col1:
            st.metric("&#128202; Total Campos", total_campos)
        
        with col2:
            st.metric("&#128197; Fechas", fechas)
        
        with col3:
            st.metric("&#128100; Nombres", nombres)
        
        with col4:
            decision = datos.get('Estado_Decision', 'N/A')
            icono = "&#9989;" if decision == "APROBADO" else "&#10060;" if decision == "NEGADO" else "&#9888;"
            st.metric("&#128221; Estado", f"{icono} {decision}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs([
            "&#128202; Datos Estructurados",
            "&#128196; Texto OCR Raw",
            "&#128190; Exportar Resultados"
        ])
        
        with tab1:
            # Organizar datos por categorias
            categorias = {
                '&#128197; Fechas': [],
                '&#128196; Documentos y Referencias': [],
                '&#128179; Identificaciones': [],
                '&#128100; Nombres y Personas': [],
                '&#128205; Ubicaciones': [],
                '&#128222; Contactos': [],
                '&#128176; Valores y Cantidades': [],
                '&#128221; Otros Datos': []
            }
            
            # Clasificar cada campo en su categoria
            for key, value in datos.items():
                if key == '_archivo':
                    continue
                    
                if 'Fecha' in key:
                    categorias['&#128197; Fechas'].append((key, value))
                elif any(x in key for x in ['Resolucion', 'Radicado', 'Documento', 'Codigo', 'Referencia']):
                    categorias['&#128196; Documentos y Referencias'].append((key, value))
                elif any(x in key for x in ['Cedula', 'NIT']):
                    categorias['&#128179; Identificaciones'].append((key, value))
                elif 'Nombre' in key:
                    categorias['&#128100; Nombres y Personas'].append((key, value))
                elif any(x in key for x in ['Direccion', 'Ciudad', 'Municipio']):
                    categorias['&#128205; Ubicaciones'].append((key, value))
                elif any(x in key for x in ['Telefono', 'Email']):
                    categorias['&#128222; Contactos'].append((key, value))
                elif any(x in key for x in ['Valor', 'Area', 'Cantidad']):
                    categorias['&#128176; Valores y Cantidades'].append((key, value))
                else:
                    categorias['&#128221; Otros Datos'].append((key, value))
            
            # Mostrar en dos columnas
            col1, col2 = st.columns(2)
            
            categorias_lista = list(categorias.items())
            mitad = (len(categorias_lista) + 1) // 2
            
            with col1:
                for categoria, items in categorias_lista[:mitad]:
                    if items:  # Solo mostrar si hay datos
                        st.markdown(f"### {categoria}")
                        for key, value in items:
                            # Formatear el nombre del campo (reemplazar _ por espacios)
                            label = key.replace('_', ' ').title()
                            st.text_input(label, value, disabled=True, key=f"cat1_{key}")
                        st.markdown("<br>", unsafe_allow_html=True)
            
            with col2:
                for categoria, items in categorias_lista[mitad:]:
                    if items:  # Solo mostrar si hay datos
                        st.markdown(f"### {categoria}")
                        for key, value in items:
                            # Formatear el nombre del campo
                            label = key.replace('_', ' ').title()
                            st.text_input(label, value, disabled=True, key=f"cat2_{key}")
                        st.markdown("<br>", unsafe_allow_html=True)
            
            # Mostrar estado/decision destacado si existe
            if 'Estado_Decision' in datos:
                decision = datos['Estado_Decision']
                if decision == "APROBADO":
                    st.success(f"&#9989; ESTADO: {decision}")
                elif decision == "NEGADO":
                    st.error(f"&#10060; ESTADO: {decision}")
                else:
                    st.warning(f"&#9888; ESTADO: {decision}")
        
        with tab2:
            st.markdown("### &#128196; Texto Raw Extraido mediante OCR")
            st.info("&#128161; Este es el texto sin procesar. Util para verificar calidad de extraccion.")
            
            col1, col2, col3 = st.columns(3)
            texto = st.session_state['texto']
            col1.metric("&#128202; Caracteres", f"{len(texto):,}")
            col2.metric("&#128196; Palabras", f"{len(texto.split()):,}")
            col3.metric("&#128221; Frases (aprox)", f"{texto.count('. '):,}")
            
            st.text_area("Contenido completo del documento", st.session_state['texto'], height=450)
        
        with tab3:
            st.markdown("### &#128190; Personaliza tu Exportacion")
            st.info("&#128161; Selecciona los campos que deseas incluir en tu archivo de exportacion")
            
            # Filtrar campos (excluir _archivo)
            campos_disponibles = [k for k in datos.keys() if not k.startswith('_')]
            
            # Crear diccionario con nombres amigables
            campos_amigables = {k: k.replace('_', ' ').title() for k in campos_disponibles}
            
            seleccion = st.multiselect(
                "Campos disponibles para exportacion",
                campos_disponibles,
                default=campos_disponibles,
                format_func=lambda x: campos_amigables[x],
                help="Selecciona uno o mas campos"
            )
            
            if seleccion:
                # Crear DataFrame con nombres de columnas amigables
                datos_export = {campos_amigables[k]: datos[k] for k in seleccion}
                df = pd.DataFrame([datos_export])
                
                st.markdown("#### &#128065; Vista Previa")
                st.dataframe(df, use_container_width=True, height=150)
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("#### &#128190; Descargar Archivo")
                
                col1, col2, col3 = st.columns([1, 1, 1])
                
                # Nombre de archivo basado en el archivo original
                nombre_base = datos.get('_archivo', 'documento').replace('.pdf', '').replace('.png', '').replace('.jpg', '')
                
                with col2:
                    csv = df.to_csv(index=False, encoding='utf-8-sig')
                    st.download_button(
                        "&#128190; DESCARGAR CSV",
                        csv,
                        f"datos_{nombre_base}.csv",
                        "text/csv",
                        use_container_width=True
                    )
                
                with col3:
                    buffer = io.BytesIO()
                    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                        df.to_excel(writer, index=False, sheet_name='Datos Extraidos')
                    st.download_button(
                        "&#128190; DESCARGAR EXCEL",
                        buffer.getvalue(),
                        f"datos_{nombre_base}.xlsx",
                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True
                    )
            else:
                st.warning("&#9888; Selecciona al menos un campo para habilitar la exportacion")
    
    # FOOTER
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; padding: 2rem; border-top: 2px solid #e2e8f0; margin-top: 3rem;">
            <p style="color: #718096; font-size: 0.9rem; margin: 0;">
                <strong style="color: #667eea;">Extractor Inteligente de Documentos v3.0 Pro</strong><br>
                Analisis Automatizado con OCR | Powered by Tesseract & Streamlit<br>
                Desarrollado por Soluciones V&G
            </p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

