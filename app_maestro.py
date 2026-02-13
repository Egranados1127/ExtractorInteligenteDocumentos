"""
🎨 INTERFAZ STREAMLIT MEJORADA - SISTEMA INTEGRADO
===================================================
Interfaz visual completa para el Extractor Maestro

Características:
- Selector de estrategia de extracción
- Comparación visual de métodos
- Panel de auto-aprendizaje
- Exportación a múltiples formatos
- Visualización de tablas extraídas
- Métricas de rendimiento
"""

import streamlit as st
import pandas as pd
from PIL import Image
import io
import time
from pathlib import Path
import json

# Importar extractor maestro
try:
    from extractor_maestro import extraer_documento, exportar_comparacion_excel, ExtractorMaestro
    from app import cargar_memoria, guardar_memoria
except ImportError as e:
    st.error(f"❌ Error importando módulos: {e}")
    st.stop()

# Configuración de página
st.set_page_config(
    page_title="⚡ DOCUX AI - Extracción Inteligente de Documentos",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados ultra-modernos - DARK THEME PREMIUM
st.markdown("""
<style>
    /* Importar fuentes premium */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&display=swap');
    
    /* Tema general - DARK MODE */
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        background-attachment: fixed;
    }
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background: linear-gradient(145deg, rgba(15, 12, 41, 0.95) 0%, rgba(36, 36, 62, 0.95) 100%);
        border-radius: 25px;
        box-shadow: 0 30px 90px rgba(0, 0, 0, 0.8),
                    0 0 50px rgba(0, 242, 234, 0.1),
                    inset 0 0 0 1px rgba(0, 242, 234, 0.2);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 242, 234, 0.1);
    }
    
    /* Header principal ULTRA IMPACTANTE */
    .main-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 4.5rem;
        font-weight: 900;
        text-align: center;
        padding: 2.5rem 0;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #00f2ea 0%, #ff00ff 50%, #00f2ea 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: glow-pulse 2s ease-in-out infinite, gradient-shift 4s linear infinite;
        background-size: 200% 200%;
        text-shadow: 0 0 40px rgba(0, 242, 234, 0.8),
                     0 0 80px rgba(255, 0, 255, 0.6);
        filter: drop-shadow(0 0 20px rgba(0, 242, 234, 0.5));
        letter-spacing: 3px;
        position: relative;
    }
    
    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes glow-pulse {
        0%, 100% {
            filter: drop-shadow(0 0 20px rgba(0, 242, 234, 0.5)) drop-shadow(0 0 40px rgba(255, 0, 255, 0.3));
        }
        50% {
            filter: drop-shadow(0 0 40px rgba(0, 242, 234, 0.8)) drop-shadow(0 0 80px rgba(255, 0, 255, 0.6));
        }
    }
    
    .subtitle {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.5rem;
        font-weight: 500;
        text-align: center;
        color: #00f2ea;
        margin-bottom: 2rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        text-shadow: 0 0 20px rgba(0, 242, 234, 0.5);
    }
    
    /* Cards de métricas PREMIUM */
    .metric-card {
        background: linear-gradient(145deg, rgba(0, 242, 234, 0.1) 0%, rgba(255, 0, 255, 0.1) 100%);
        padding: 1.8rem;
        border-radius: 20px;
        color: #00f2ea;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6),
                    0 0 30px rgba(0, 242, 234, 0.2),
                    inset 0 0 0 1px rgba(0, 242, 234, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid rgba(0, 242, 234, 0.2);
        margin: 0.5rem 0;
        backdrop-filter: blur(15px);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(0, 242, 234, 0.1), transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .metric-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8),
                    0 0 50px rgba(0, 242, 234, 0.4),
                    inset 0 0 0 1px rgba(0, 242, 234, 0.5);
        border-color: rgba(0, 242, 234, 0.5);
    }
    
    .metric-value {
        font-size: 3rem;
        font-weight: 900;
        font-family: 'Orbitron', sans-serif;
        margin: 0.5rem 0;
        color: #ff00ff;
        text-shadow: 0 0 20px rgba(255, 0, 255, 0.6);
        position: relative;
        z-index: 1;
    }
    
    .metric-label {
        font-size: 0.85rem;
        opacity: 0.8;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: 'Rajdhani', sans-serif;
        color: #00f2ea;
        position: relative;
        z-index: 1;
    }
    
    /* Success/Warning boxes PREMIUM */
    .success-box {
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.2) 0%, rgba(0, 255, 135, 0.2) 100%);
        border: 1px solid rgba(0, 242, 234, 0.4);
        color: #ffffff;
        padding: 1.8rem;
        border-radius: 18px;
        margin: 1.5rem 0;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5),
                    0 0 30px rgba(0, 242, 234, 0.2);
        font-family: 'Rajdhani', sans-serif;
        backdrop-filter: blur(15px);
    }
    
    .success-box h3 {
        margin: 0 0 0.5rem 0;
        font-weight: 600;
        color: #00f2ea;
    }
    
    .warning-box {
        background: linear-gradient(135deg, rgba(255, 0, 255, 0.2) 0%, rgba(255, 0, 135, 0.2) 100%);
        border: 1px solid rgba(255, 0, 255, 0.4);
        color: #ffffff;
        padding: 1.8rem;
        border-radius: 18px;
        margin: 1.5rem 0;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5),
                    0 0 30px rgba(255, 0, 255, 0.2);
        font-family: 'Rajdhani', sans-serif;
        backdrop-filter: blur(15px);
    }
    
    .warning-box h3 {
        margin: 0 0 0.5rem 0;
        font-weight: 600;
        color: #ff00ff;
    }
    
    /* Botones PREMIUM con efectos neón */
    .stButton>button {
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.2) 0%, rgba(255, 0, 255, 0.2) 100%);
        color: #ffffff;
        border: 2px solid #00f2ea;
        border-radius: 15px;
        padding: 1rem 2.5rem;
        font-weight: 700;
        font-family: 'Rajdhani', sans-serif;
        box-shadow: 0 5px 25px rgba(0, 0, 0, 0.5),
                    0 0 20px rgba(0, 242, 234, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 1rem;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.7),
                    0 0 40px rgba(0, 242, 234, 0.6);
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.3) 0%, rgba(255, 0, 255, 0.3) 100%);
        border-color: #ff00ff;
        color: #ffffff;
    }
    
    /* Botones de Descarga PREMIUM */
    .stDownloadButton>button {
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.2) 0%, rgba(255, 0, 255, 0.2) 100%);
        color: #ffffff !important;
        border: 2px solid #00f2ea;
        border-radius: 15px;
        padding: 1rem 2.5rem;
        font-weight: 700;
        font-family: 'Rajdhani', sans-serif;
        box-shadow: 0 5px 25px rgba(0, 0, 0, 0.5),
                    0 0 20px rgba(0, 242, 234, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 1rem;
    }
    
    .stDownloadButton>button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.7),
                    0 0 40px rgba(0, 242, 234, 0.6);
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.3) 0%, rgba(255, 0, 255, 0.3) 100%);
        border-color: #ff00ff;
        color: #ffffff !important;
    }
    
    .stDownloadButton>button * {
        color: #ffffff !important;
    }
    
    /* Selectbox PREMIUM */
    .stSelectbox {
        font-family: 'Rajdhani', sans-serif;
    }
    
    .stSelectbox > div > div {
        background: rgba(0, 242, 234, 0.1);
        border: 1px solid rgba(0, 242, 234, 0.3);
        color: #ffffff;
    }
    
    .stSelectbox label {
        color: rgba(255, 255, 255, 0.95) !important;
    }
    
    /* DROPDOWN SYSTEM - EMPUJA ELEMENTOS EN LUGAR DE SUPERPONERLOS */
    
    /* Contenedores de elementos que deben moverse cuando hay dropdown abierto */
    .stElementContainer,
    .element-container,
    .stColumn > div,
    .stForm,
    .stExpander,
    .stTabs,
    .stButton,
    .stDownloadButton,
    [data-testid="element-container"] {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        transform-origin: top center !important;
    }
    
    /* Detectar cuando un dropdown está abierto y empujar elementos siguientes */
    .stSelectbox:has([aria-expanded="true"]) ~ .stElementContainer,
    .stSelectbox:has([aria-expanded="true"]) ~ .element-container,
    .stSelectbox:has([role="listbox"]) ~ .stElementContainer,
    .stSelectbox:has([role="listbox"]) ~ .element-container,
    .stSelectbox:has([data-baseweb="select"][aria-expanded="true"]) ~ .stElementContainer,
    .stSelectbox:has([data-baseweb="select"][aria-expanded="true"]) ~ .element-container,
    
    /* Empujar hermanos siguientes cuando hay dropdown expandido */
    .stSelectbox[data-dropdown-open="true"] ~ *,
    .element-container:has(.stSelectbox [aria-expanded="true"]) ~ .element-container,
    .element-container:has(.stSelectbox [role="listbox"]) ~ .element-container,
    
    /* Empujar todos los elementos después de un selectbox con menú abierto */
    .element-container:has([data-baseweb="select"][aria-expanded="true"]) ~ .element-container,
    .element-container:has([class*="Menu"]) ~ .element-container {
        margin-top: 320px !important;
        transform: translateY(20px) !important;
    }
    
    /* DROPDOWN OPTIONS - SIN Z-INDEX ALTO, POSICIÓN NATURAL */
    .stSelectbox option,
    [data-baseweb="select"] ul,
    [data-baseweb="select"] ul li,
    [data-baseweb="select"] [role="option"],
    [data-baseweb="menu"] ul,
    [data-baseweb="menu"] ul li,
    [data-baseweb="menu"] [role="option"],
    div[role="listbox"],
    div[role="listbox"] div,
    div[role="option"],
    .css-1uccc91-Menu,
    .css-1n7v3ny-Menu,
    [class*="Menu"],
    [class*="option"],
    [class*="dropdown"] {
        background: rgba(15, 12, 41, 0.95) !important;
        color: #ffffff !important;
        border: 2px solid rgba(0, 242, 234, 0.6) !important;
        border-radius: 12px !important;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.8),
                    0 0 30px rgba(0, 242, 234, 0.4),
                    0 0 60px rgba(255, 0, 255, 0.2) !important;
        backdrop-filter: blur(20px) !important;
        /* REMOVIDO: z-index alto para no superponer */
        z-index: 10 !important;
        position: relative !important;
        margin-top: 8px !important;
        margin-bottom: 16px !important;
        padding: 0.5rem !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 600 !important;
        max-height: 300px !important;
        min-height: 200px !important;
        overflow-y: auto !important;
    }
    
    /* Opciones individuales del dropdown */
    [data-baseweb="select"] [role="option"],
    [data-baseweb="menu"] [role="option"],
    div[role="option"],
    .stSelectbox option,
    [class*="option"]:not([class*="container"]) {
        background: rgba(15, 12, 41, 0.8) !important;
        color: rgba(255, 255, 255, 0.95) !important;
        padding: 1rem 1.5rem !important;
        margin: 4px 0 !important;
        border-radius: 8px !important;
        border: 1px solid transparent !important;
        transition: all 0.3s ease !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        cursor: pointer !important;
    }
    
    /* Hover effect para opciones del dropdown */
    [data-baseweb="select"] [role="option"]:hover,
    [data-baseweb="menu"] [role="option"]:hover,
    div[role="option"]:hover,
    .stSelectbox option:hover,
    [class*="option"]:not([class*="container"]):hover {
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.3) 0%, rgba(255, 0, 255, 0.3) 100%) !important;
        color: #ffffff !important;
        border-color: rgba(0, 242, 234, 0.8) !important;
        box-shadow: 0 5px 15px rgba(0, 242, 234, 0.4) !important;
        transform: translateX(5px) !important;
    }
    
    /* Opción seleccionada */
    [aria-selected="true"][role="option"],
    [data-baseweb="select"] [aria-selected="true"],
    [data-baseweb="menu"] [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.4) 0%, rgba(255, 0, 255, 0.4) 100%) !important;
        color: #ffffff !important;
        border-color: rgba(255, 0, 255, 0.8) !important;
        font-weight: 700 !important;
    }
    
    /* Container del dropdown - posición natural */
    [data-baseweb="select"],
    [data-baseweb="menu"],
    .stSelectbox [role="listbox"],
    .stSelectbox > div,
    [class*="Select"]:not([class*="container"]) {
        z-index: 10 !important;
        position: relative !important;
    }
    
    /* Tabs PREMIUM con efecto neón */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1.5rem;
        background: transparent;
        border-bottom: 2px solid rgba(0, 242, 234, 0.2);
    }
    
    .stTabs [data-baseweb="tab"] {
        font-family: 'Rajdhani', sans-serif;
        font-weight: 700;
        font-size: 1.1rem;
        border-radius: 12px 12px 0 0;
        padding: 1.2rem 2.5rem;
        background: rgba(0, 242, 234, 0.05);
        color: rgba(255, 255, 255, 0.6);
        border: 1px solid rgba(0, 242, 234, 0.2);
        border-bottom: none;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(0, 242, 234, 0.15);
        color: #ffffff;
        box-shadow: 0 0 20px rgba(0, 242, 234, 0.3);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.3) 0%, rgba(255, 0, 255, 0.3) 100%);
        color: #ffffff;
        border-color: #00f2ea;
        box-shadow: 0 0 30px rgba(0, 242, 234, 0.4),
                    0 -5px 20px rgba(0, 242, 234, 0.2);
    }
    
    /* Tab Panels - Asegurar texto visible */
    [data-baseweb="tab-panel"] p,
    [data-baseweb="tab-panel"] span,
    [data-baseweb="tab-panel"] div,
    [data-baseweb="tab-panel"] label {
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    /* Tab panels específicos (Comparar Métodos y Memoria de Aprendizaje) */
    #tabs-bui2-tabpanel-1 p,
    #tabs-bui2-tabpanel-2 p,
    #tabs-bui2-tabpanel-1 span,
    #tabs-bui2-tabpanel-2 span,
    #tabs-bui2-tabpanel-1 div,
    #tabs-bui2-tabpanel-2 div,
    #tabs-bui5-tabpanel-1 p,
    #tabs-bui5-tabpanel-2 p,
    #tabs-bui5-tabpanel-1 span,
    #tabs-bui5-tabpanel-2 span,
    #tabs-bui5-tabpanel-1 div,
    #tabs-bui5-tabpanel-2 div {
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    /* Selectores específicos problemáticos */
    #tabs-bui2-tabpanel-1 > div > div.stElementContainer p,
    #tabs-bui2-tabpanel-2 > div > div.stElementContainer p,
    #tabs-bui5-tabpanel-1 > div > div.stElementContainer p,
    #tabs-bui5-tabpanel-2 > div > div.stElementContainer p,
    #tabs-bui5-tabpanel-1 > div > div.stElementContainer.element-container.st-emotion-cache-1vo6xi6.e12zf7d51 > div > div > div > div > div > div > p,
    #tabs-bui5-tabpanel-2 > div > div.stElementContainer.element-container.st-emotion-cache-1vo6xi6.e12zf7d51 > div > div > div > div > div > div > p,
    .stElementContainer p,
    .element-container p,
    /* Selector específico con problema de visibilidad */
    #bui21val-5,
    #bui21val-5 *,
    #bui21val-5 input,
    #bui21val-5 label,
    #bui21val-5 p,
    #bui21val-5 span,
    #bui21val-5 div {
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    /* Sidebar PREMIUM con tema oscuro */
    .css-1d391kg {
        background: linear-gradient(180deg, #0f0c29 0%, #302b63 100%);
        background-attachment: fixed;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0c29 0%, #24243e 100%);
        border-right: 2px solid rgba(0, 242, 234, 0.2);
    }
    
    [data-testid="stSidebar"] .block-container {
        background: rgba(0, 242, 234, 0.05);
        backdrop-filter: blur(20px);
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div {
        color: rgba(255, 255, 255, 0.95) !important;
        font-family: 'Rajdhani', sans-serif;
        text-shadow: none;
    }
    
    /* Botón de toggle del sidebar - OCULTAR COMPLETAMENTE */
    button[kind="header"], 
    button[data-testid="collapsedControl"],
    .css-1vq4p4l,
    .css-1d391kg button,
    [data-testid="stSidebarNav"] button,
    .st-emotion-cache-1vq4p4l,
    button[aria-label*="sidebar"],
    button[aria-label*="navigation"],
    .stSidebarNav button,
    /* Selectores específicos para el botón de colapsar */
    #root > div:nth-child(1) > div.withScreencast > div > div > button,
    .withScreencast > div > div > button,
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-10p9htt.e9ic3ti4 > div.st-emotion-cache-1pma7n.e9ic3ti10 > button,
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-10p9htt.e9ic3ti4 > div.st-emotion-cache-1pma7n.e9ic3ti10 > button > span,
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-10p9htt.e9ic3ti4 > div.st-emotion-cache-1pma7n.e9ic3ti10 > button > span > span,
    /* SELECTOR ESPECÍFICO QUE EL USUARIO QUIERE OCULTAR */
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-10p9htt.e9ic3ti4 > div.st-emotion-cache-1pma7n.e9ic3ti10 > button > span > span {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
        position: absolute !important;
        left: -9999px !important;
        top: -9999px !important;
        width: 0 !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Hover effect para el botón de toggle */
    button[kind="header"]:hover, 
    button[data-testid="collapsedControl"]:hover,
    .css-1vq4p4l:hover,
    .css-1d391kg button:hover,
    [data-testid="stSidebarNav"] button:hover,
    .st-emotion-cache-1vq4p4l:hover,
    button[aria-label*="sidebar"]:hover,
    button[aria-label*="navigation"]:hover,
    .stSidebarNav button:hover,
    #root > div:nth-child(1) > div.withScreencast > div > div > button:hover,
    .withScreencast > div > div > button:hover,
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-10p9htt.e9ic3ti4 > div.st-emotion-cache-1pma7n.e9ic3ti10 > button:hover,
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-10p9htt.e9ic3ti4 > div.st-emotion-cache-1pma7n.e9ic3ti10 > button > span:hover,
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-10p9htt.e9ic3ti4 > div.st-emotion-cache-1pma7n.e9ic3ti10 > button > span > span:hover {
        background: rgba(0, 242, 234, 1) !important;
        color: #000000 !important;
        box-shadow: 0 0 25px rgba(0, 242, 234, 0.8) !important;
        transform: scale(1.05) !important;
    }
    
    /* Icono de flecha visible */
    button[kind="header"] svg, 
    button[data-testid="collapsedControl"] svg,
    .css-1vq4p4l svg,
    .css-1d391kg button svg,
    [data-testid="stSidebarNav"] button svg,
    button[aria-label*="sidebar"] svg,
    button[aria-label*="navigation"] svg,
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-10p9htt.e9ic3ti4 > div.st-emotion-cache-1pma7n.e9ic3ti10 > button svg,
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-10p9htt.e9ic3ti4 > div.st-emotion-cache-1pma7n.e9ic3ti10 > button > span svg,
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-10p9htt.e9ic3ti4 > div.st-emotion-cache-1pma7n.e9ic3ti10 > button > span > span svg {
        fill: #ffffff !important;
        stroke: #ffffff !important;
        color: #ffffff !important;
        width: 20px !important;
        height: 20px !important;
    }
    
    /* BOTÓN VISIBLE CUANDO SIDEBAR ESTÁ COLAPSADO/OCULTO */
    .stSidebar--collapsed button,
    .stApp--sidebarCollapsed button[kind="header"],
    .stApp--sidebarCollapsed button[data-testid="collapsedControl"],
    /* Selectores específicos para sidebar colapsado */
    body[class*="collapsed"] button,
    div[class*="collapsed"] button,
    .st-emotion-cache-1cypcdb button,
    .st-emotion-cache-16txtl3 button,
    /* Botón cuando no hay sidebar visible */
    .withScreencast > div > div > button:only-child,
    #root > div:nth-child(1) > div.withScreencast > div > div > button:first-child {
        background: rgba(255, 0, 255, 0.9) !important;
        color: #ffffff !important;
        border: 3px solid rgba(255, 0, 255, 0.8) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        margin: 12px !important;
        font-size: 24px !important;
        font-weight: 900 !important;
        box-shadow: 0 0 30px rgba(255, 0, 255, 0.6), 
                    0 0 15px rgba(0, 242, 234, 0.4) !important;
        visibility: visible !important;
        opacity: 1 !important;
        display: flex !important;
        z-index: 99999 !important;
        position: fixed !important;
        top: 20px !important;
        left: 20px !important;
        min-width: 50px !important;
        min-height: 50px !important;
        cursor: pointer !important;
        animation: pulseGlow 2s infinite !important;
    }
    
    /* Animación de pulso para botón colapsado */
    @keyframes pulseGlow {
        0% { box-shadow: 0 0 20px rgba(255, 0, 255, 0.6); }
        50% { box-shadow: 0 0 40px rgba(255, 0, 255, 0.9), 0 0 20px rgba(0, 242, 234, 0.6); }
        100% { box-shadow: 0 0 20px rgba(255, 0, 255, 0.6); }
    }
    
    /* Hover super intenso para botón colapsado */
    .stSidebar--collapsed button:hover,
    .stApp--sidebarCollapsed button:hover,
    body[class*="collapsed"] button:hover,
    div[class*="collapsed"] button:hover,
    .st-emotion-cache-1cypcdb button:hover,
    .st-emotion-cache-16txtl3 button:hover,
    .withScreencast > div > div > button:only-child:hover,
    #root > div:nth-child(1) > div.withScreencast > div > div > button:first-child:hover {
        background: rgba(255, 0, 255, 1) !important;
        color: #000000 !important;
        box-shadow: 0 0 50px rgba(255, 0, 255, 1), 
                    0 0 30px rgba(0, 242, 234, 0.8) !important;
        transform: scale(1.2) !important;
        border-color: rgba(0, 242, 234, 1) !important;
    }
    
    /* SVG del botón colapsado súper visible */
    .stSidebar--collapsed button svg,
    .stApp--sidebarCollapsed button svg,
    body[class*="collapsed"] button svg,
    div[class*="collapsed"] button svg,
    .withScreencast > div > div > button:only-child svg,
    #root > div:nth-child(1) > div.withScreencast > div > div > button:first-child svg {
        fill: #ffffff !important;
        stroke: #ffffff !important;
        color: #ffffff !important;
        width: 30px !important;
        height: 30px !important;
        filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.8)) !important;
    }
    
    /* FLECHA PERSONALIZADA PARA SIDEBAR - MÁS GRANDE Y VISIBLE */
    .custom-sidebar-toggle {
        position: fixed !important;
        top: 15px !important;
        left: 15px !important;
        width: 60px !important;
        height: 60px !important;
        background: linear-gradient(135deg, rgba(255, 0, 255, 0.95) 0%, rgba(0, 242, 234, 0.9) 100%) !important;
        border: 4px solid rgba(255, 255, 255, 0.9) !important;
        border-radius: 50% !important;
        cursor: pointer !important;
        z-index: 999999999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0 0 40px rgba(255, 0, 255, 0.8), 
                    0 0 25px rgba(0, 242, 234, 0.6),
                    0 5px 15px rgba(0, 0, 0, 0.4),
                    inset 0 0 30px rgba(255, 255, 255, 0.2) !important;
        transition: all 0.3s ease !important;
        animation: superPulse 2s infinite !important;
        font-family: Arial, sans-serif !important;
    }
    
    .custom-sidebar-toggle:hover {
        transform: scale(1.2) !important;
        background: linear-gradient(135deg, rgba(255, 0, 255, 1) 0%, rgba(0, 242, 234, 1) 100%) !important;
        box-shadow: 0 0 60px rgba(255, 0, 255, 1), 
                    0 0 40px rgba(0, 242, 234, 0.8),
                    0 10px 25px rgba(0, 0, 0, 0.6),
                    inset 0 0 40px rgba(255, 255, 255, 0.3) !important;
        border-color: rgba(255, 255, 255, 1) !important;
    }
    
    /* Flecha dentro del botón - MÁS GRANDE */
    .custom-sidebar-toggle::before {
        content: '◀' !important;
        font-size: 32px !important;
        font-weight: 900 !important;
        color: #ffffff !important;
        text-shadow: 0 0 15px rgba(255, 255, 255, 1),
                     0 0 25px rgba(0, 242, 234, 0.8),
                     0 3px 6px rgba(0, 0, 0, 0.5) !important;
        transform: rotate(0deg) !important;
        transition: all 0.3s ease !important;
        line-height: 1 !important;
    }
    
    /* Flecha cuando sidebar está abierto */
    .custom-sidebar-toggle.sidebar-open::before {
        content: '◀' !important;
        transform: rotate(0deg) !important;
    }
    
    /* Flecha cuando sidebar está cerrado */
    .custom-sidebar-toggle.sidebar-closed::before {
        content: '▶' !important;
        transform: rotate(0deg) !important;
    }
    
    /* Animación super visible */
    @keyframes superPulse {
        0% { 
            box-shadow: 0 0 30px rgba(255, 0, 255, 0.6), 
                        0 0 20px rgba(0, 242, 234, 0.4); 
        }
        50% { 
            box-shadow: 0 0 50px rgba(255, 0, 255, 1), 
                        0 0 35px rgba(0, 242, 234, 0.8),
                        inset 0 0 20px rgba(255, 255, 255, 0.2); 
        }
        100% { 
            box-shadow: 0 0 30px rgba(255, 0, 255, 0.6), 
                        0 0 20px rgba(0, 242, 234, 0.4); 
        }
    }
    
    /* SIDEBAR COLLAPSE SUPPORT - Manipulación directa */
    .sidebar-collapsed [data-testid="stSidebar"] {
        transform: translateX(-100%) !important;
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    .sidebar-collapsed .block-container {
        margin-left: 0 !important;
        transition: margin-left 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Cuando el sidebar está visible, ajustar el contenido principal */
    [data-testid="stSidebar"]:not([style*="translateX(-"]) ~ .stMainBlockContainer,
    [data-testid="stSidebar"]:not([style*="translateX(-"]) ~ * .stMainBlockContainer {
        margin-left: 0 !important;
        transition: margin-left 0.3s ease !important;
    }
    
    /* Overlay para cerrar sidebar en mobile */
    .sidebar-overlay {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        background: rgba(0, 0, 0, 0.5) !important;
        z-index: 9999 !important;
        backdrop-filter: blur(3px) !important;
        opacity: 0 !important;
        pointer-events: none !important;
        transition: opacity 0.3s ease !important;
    }
    
    .sidebar-overlay.active {
        opacity: 1 !important;
        pointer-events: all !important;
    }
    
    /* Tooltip para la flecha */
    .custom-sidebar-toggle:hover::after {
        content: 'Panel de Control' !important;
        position: absolute !important;
        top: -40px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        background: rgba(0, 0, 0, 0.9) !important;
        color: #00f2ea !important;
        padding: 8px 12px !important;
        border-radius: 8px !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        white-space: nowrap !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
        border: 1px solid rgba(0, 242, 234, 0.5) !important;
        z-index: 100000 !important;
    }
    
    /* Dataframe PREMIUM */
    .dataframe {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6),
                    0 0 20px rgba(0, 242, 234, 0.2);
        border: 1px solid rgba(0, 242, 234, 0.2);
    }
    
    .dataframe th {
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.3) 0%, rgba(255, 0, 255, 0.3) 100%) !important;
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
        border-color: rgba(0, 242, 234, 0.2) !important;
    }
    
    .dataframe td {
        background: rgba(15, 12, 41, 0.6) !important;
        color: rgba(255, 255, 255, 0.95) !important;
        font-family: 'Rajdhani', sans-serif !important;
        border-color: rgba(0, 242, 234, 0.1) !important;
    }
    
    /* Controles de Dataframe - Botones de descarga/fullscreen */
    [data-testid="stDataFrame"] button,
    [data-testid="stDataFrame"] [role="button"],
    .stDataFrame button,
    div[data-testid="stDataFrame"] button {
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.2) 0%, rgba(255, 0, 255, 0.2) 100%) !important;
        color: #ffffff !important;
        border: 1px solid rgba(0, 242, 234, 0.4) !important;
        border-radius: 8px !important;
        padding: 0.5rem !important;
    }
    
    [data-testid="stDataFrame"] button:hover,
    .stDataFrame button:hover {
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.4) 0%, rgba(255, 0, 255, 0.4) 100%) !important;
        border-color: #00f2ea !important;
        box-shadow: 0 0 15px rgba(0, 242, 234, 0.3) !important;
    }
    
    [data-testid="stDataFrame"] svg,
    .stDataFrame svg {
        color: #ffffff !important;
        fill: #ffffff !important;
    }
    
    /* Headers y controles interactivos de tabla */
    [data-testid="stDataFrame"] [role="columnheader"],
    .stDataFrame [role="columnheader"] {
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.3) 0%, rgba(255, 0, 255, 0.3) 100%) !important;
        color: #ffffff !important;
    }
    
    /* Toolbar de dataframe */
    [data-testid="stDataFrameToolbar"],
    .dataframe-toolbar {
        background: rgba(15, 12, 41, 0.8) !important;
        border: 1px solid rgba(0, 242, 234, 0.2) !important;
    }
    
    /* File uploader PREMIUM */
    .stFileUploader {
        border: 2px dashed rgba(0, 242, 234, 0.5);
        border-radius: 20px;
        padding: 2.5rem;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .stFileUploader:hover {
        border-color: #00f2ea;
        background: rgba(255, 255, 255, 1);
        box-shadow: 0 0 30px rgba(0, 242, 234, 0.3);
    }
    
    .stFileUploader label,
    .stFileUploader span,
    .stFileUploader p,
    .stFileUploader button {
        color: #1e3a8a !important;
        font-weight: 600 !important;
    }
    
    .stFileUploader small {
        color: #64748b !important;
    }
    
    /* Radio buttons PREMIUM */
    .stRadio > label {
        color: rgba(255, 255, 255, 0.95) !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 600 !important;
    }
    
    .stRadio > div {
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    .stRadio label {
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    /* Text inputs PREMIUM */
    input, textarea, .stTextInput > div > div > input {
        background: rgba(0, 242, 234, 0.1) !important;
        border: 1px solid rgba(0, 242, 234, 0.3) !important;
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif !important;
    }
    
    /* Placeholder text */
    input::placeholder, textarea::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }
    
    /* Labels y textos generales - TODOS CLAROS */
    label, p, span, div {
        font-family: 'Rajdhani', sans-serif;
        color: rgba(255, 255, 255, 0.9);
    }
    
    /* Textos específicos */
    .stMarkdown, .stMarkdown p, .stMarkdown span {
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #00f2ea !important;
        font-family: 'Orbitron', sans-serif;
        text-shadow: 0 0 10px rgba(0, 242, 234, 0.3);
    }
    
    /* Captions de gráficas y elementos */
    .caption, [data-testid="stCaptionContainer"], .element-container .caption {
        color: rgba(255, 255, 255, 0.7) !important;
        font-size: 0.85rem !important;
    }
    
    /* Métricas de Streamlit */
    [data-testid="stMetric"], .stMetric {
        background: rgba(0, 242, 234, 0.1) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        border: 1px solid rgba(0, 242, 234, 0.2) !important;
    }
    
    [data-testid="stMetricLabel"], .stMetric label {
        color: rgba(255, 255, 255, 0.8) !important;
        font-size: 0.9rem !important;
    }
    
    [data-testid="stMetricValue"], .stMetric [data-testid="stMetricValue"] {
        color: #00f2ea !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stMetricDelta"], .stMetric [data-testid="stMetricDelta"] {
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    /* Divider */
    hr, .stDivider {
        border-color: rgba(0, 242, 234, 0.3) !important;
    }
    
    /* Expander PREMIUM */
    .streamlit-expanderHeader {
        background: rgba(0, 242, 234, 0.1);
        border: 1px solid rgba(0, 242, 234, 0.2);
        border-radius: 12px;
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif;
        font-weight: 700;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(0, 242, 234, 0.2);
        box-shadow: 0 0 20px rgba(0, 242, 234, 0.2);
        color: #00f2ea !important;
    }
    
    /* Configuración Avanzada - Texto estrecho corregido */
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-1r1cntt.e9ic3ti1 > div > div > div:nth-child(3) > div > details > summary > span > div > div > p,
    details > summary > span > div > div > p,
    .st-emotion-cache-155jwzh details summary p,
    .st-emotion-cache-1r1cntt details summary p {
        color: rgba(255, 255, 255, 0.95) !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        line-height: 1.5 !important;
        padding: 8px 16px !important;
        margin: 0 !important;
        min-width: 200px !important;
        width: auto !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        font-family: 'Rajdhani', sans-serif !important;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.5) !important;
    }
    
    /* Summary container mejorado */
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-1r1cntt.e9ic3ti1 > div > div > div:nth-child(3) > div > details > summary,
    .st-emotion-cache-155jwzh details summary,
    .st-emotion-cache-1r1cntt details summary {
        background: rgba(0, 242, 234, 0.1) !important;
        border: 1px solid rgba(0, 242, 234, 0.3) !important;
        border-radius: 12px !important;
        padding: 12px 20px !important;
        margin: 8px 0 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        min-height: 44px !important;
        display: flex !important;
        align-items: center !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }
    
    /* Hover effect para summary */
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-1r1cntt.e9ic3ti1 > div > div > div:nth-child(3) > div > details > summary:hover,
    .st-emotion-cache-155jwzh details summary:hover,
    .st-emotion-cache-1r1cntt details summary:hover {
        background: rgba(0, 242, 234, 0.2) !important;
        box-shadow: 0 0 20px rgba(0, 242, 234, 0.2) !important;
        border-color: rgba(0, 242, 234, 0.6) !important;
    }
    
    /* Animación de entrada desde abajo */
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Efectos de glassmorphism PREMIUM */
    .glass-card {
        background: rgba(0, 242, 234, 0.08);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(0, 242, 234, 0.2);
        padding: 2rem;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.6),
                    0 0 30px rgba(0, 242, 234, 0.1);
    }
    
    /* Progress bar PREMIUM */
    .stProgress > div > div {
        background: linear-gradient(90deg, #00f2ea 0%, #ff00ff 100%);
        box-shadow: 0 0 20px rgba(0, 242, 234, 0.5);
    }
    
    /* RESPONSIVE DESIGN - Mobile First */
    @media only screen and (max-width: 768px) {
        /* Header más pequeño en móvil */
        .main-header {
            font-size: 2.5rem !important;
            padding: 1.5rem 0 !important;
            letter-spacing: 1px !important;
        }
        
        .subtitle {
            font-size: 1rem !important;
        }
        
        /* Contenedor con menos padding */
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }
        
        /* Cards más compactas */
        .metric-card {
            padding: 1rem !important;
            margin-bottom: 1rem !important;
        }
        
        /* File uploader optimizado para móvil */
        .stFileUploader {
            padding: 1rem !important;
        }
        
        /* Radio buttons en columna en vez de horizontal */
        [data-testid="stHorizontalBlock"] {
            flex-direction: column !important;
            gap: 0.5rem !important;
        }
        
        /* Botones más grandes para touch */
        .stButton button {
            padding: 1rem 2rem !important;
            font-size: 1.1rem !important;
            width: 100% !important;
        }
        
        /* Camera input responsive */
        [data-testid="stCameraInput"] {
            width: 100% !important;
        }
        
        [data-testid="stCameraInput"] video {
            max-width: 100% !important;
            border-radius: 15px !important;
        }
    }
    
    /* Mensajes de Streamlit - Fondos claros con texto oscuro */
    .stAlert, [data-testid="stAlert"] {
        color: #1e293b !important;
    }
    
    /* Header superior de Streamlit - ocultar o hacer transparente */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > header > div,
    header[data-testid="stHeader"],
    [data-testid="stHeader"],
    .stApp > header {
        background: transparent !important;
        visibility: hidden !important;
        display: none !important;
    }
    
    /* Toolbar de Streamlit - ocultar */
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    .stDeployButton {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* Selector específico a ocultar */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stMainBlockContainer.block-container.st-emotion-cache-zy6yx3.e1td4qo64 > div > div:nth-child(5) > div > div > div > div {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }
    
    /* Selector adicional del expander a ocultar */
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.st-emotion-cache-155jwzh.e9ic3ti2 > div.st-emotion-cache-1r1cntt.e9ic3ti1 > div > div > div:nth-child(3) > div > details > summary > span > span > span {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }
    
    /* Elementos de código y texto preformateado */
    pre, code, 
    .stCodeBlock code,
    [data-testid="stCode"] code,
    .st-emotion-cache-acwcvw code,
    #root pre code,
    #root pre div code,
    .stMainBlockContainer pre code,
    .stMainBlockContainer pre div code {
        background: rgba(15, 12, 41, 0.8) !important;
        color: #00f2ea !important;
        font-family: 'Courier New', monospace !important;
        padding: 0.5rem !important;
        border-radius: 8px !important;
        border: 1px solid rgba(0, 242, 234, 0.3) !important;
        word-wrap: break-word !important;
        white-space: pre-wrap !important;
    }
    
    /* Selector específico problemático */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stMainBlockContainer code,
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stMainBlockContainer pre code,
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stMainBlockContainer pre div code {
        color: #00f2ea !important;
        background: rgba(15, 12, 41, 0.9) !important;
    }
    
    /* Pre containers */
    pre {
        background: rgba(15, 12, 41, 0.6) !important;
        border: 1px solid rgba(0, 242, 234, 0.2) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        margin: 1rem 0 !important;
    }
    
    /* Fix text visibility for selector #root > div:nth-child(2) > div > div > div > div */
    #root > div:nth-child(2) > div > div > div > div,
    #root > div:nth-child(2) > div > div > div > div *,
    #root > div:nth-child(2) > div > div > div > div p,
    #root > div:nth-child(2) > div > div > div > div span,
    #root > div:nth-child(2) > div > div > div > div div,
    #root > div:nth-child(2) > div > div > div > div label,
    #root > div:nth-child(2) > div > div > div > div h1,
    #root > div:nth-child(2) > div > div > div > div h2,
    #root > div:nth-child(2) > div > div > div > div h3,
    #root > div:nth-child(2) > div > div > div > div h4,
    #root > div:nth-child(2) > div > div > div > div h5,
    #root > div:nth-child(2) > div > div > div > div h6,
    #root > div:nth-child(2) > div > div > div > div text {
        color: rgba(255, 255, 255, 0.95) !important;
        background-color: transparent !important;
        opacity: 1 !important;
        visibility: visible !important;
        text-shadow: 0 0 3px rgba(0, 242, 234, 0.3) !important;
    }
    
    .stAlert p, [data-testid="stAlert"] p,
    .stAlert span, [data-testid="stAlert"] span,
    .stAlert div, [data-testid="stAlert"] div {
        color: #1e293b !important;
    }
    
    /* Success messages */
    [data-testid="stSuccess"],
    .element-container:has([data-testid="stSuccess"]) {
        background-color: #d1fae5 !important;
    }
    
    [data-testid="stSuccess"] * {
        color: #065f46 !important;
    }
    
    /* Info messages */
    [data-testid="stInfo"],
    .element-container:has([data-testid="stInfo"]) {
        background-color: #dbeafe !important;
    }
    
    [data-testid="stInfo"] * {
        color: #1e40af !important;
    }
    
    /* Warning messages */
    [data-testid="stWarning"],
    .element-container:has([data-testid="stWarning"]) {
        background-color: #fef3c7 !important;
    }
    
    [data-testid="stWarning"] * {
        color: #92400e !important;
    }
    
    /* Error messages */
    [data-testid="stError"],
    .element-container:has([data-testid="stError"]) {
        background-color: #fee2e2 !important;
    }
    
    [data-testid="stError"] * {
        color: #991b1b !important;
    }
    
    /* Tablets */
    @media only screen and (min-width: 769px) and (max-width: 1024px) {
        .main-header {
            font-size: 2.5rem !important;
        }
        
        .block-container {
            padding: 1.5rem !important;
        }
    }
    
    /* Optimizaciones para touch devices */
    @media (hover: none) and (pointer: coarse) {
        /* Aumentar área táctil */
        button, a, input, select {
            min-height: 44px !important;
        }
        
        /* Preview de imagen más grande en touch */
        .stImage img {
            border-radius: 15px !important;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2) !important;
        }
    }

""", unsafe_allow_html=True)

# Header principal con efecto impactante PREMIUM
st.markdown("""
<div style="text-align: center; margin-bottom: 3rem; position: relative;">
    <h1 class="main-header">⚡ DOCUX AI ⚡</h1>
    <p class="subtitle">🚀 INTELIGENCIA ARTIFICIAL DE ÚLTIMA GENERACIÓN EN EXTRACCIÓN DOCUMENTAL 🚀</p>
    <div style="display: flex; justify-content: center; gap: 1.5rem; margin-top: 2rem; flex-wrap: wrap;">
        <span style="background: linear-gradient(135deg, rgba(0, 242, 234, 0.2) 0%, rgba(0, 242, 234, 0.3) 100%); 
                     color: #00f2ea; 
                     padding: 0.8rem 2rem; 
                     border-radius: 30px; 
                     font-family: 'Rajdhani', sans-serif; 
                     font-size: 1rem; 
                     font-weight: 700;
                     border: 2px solid #00f2ea;
                     box-shadow: 0 0 25px rgba(0, 242, 234, 0.4);
                     text-transform: uppercase;
                     letter-spacing: 2px;">
            🧠 6 Estrategias IA
        </span>
        <span style="background: linear-gradient(135deg, rgba(255, 0, 255, 0.2) 0%, rgba(255, 0, 255, 0.3) 100%); 
                     color: #ff00ff; 
                     padding: 0.8rem 2rem; 
                     border-radius: 30px; 
                     font-family: 'Rajdhani', sans-serif; 
                     font-size: 1rem; 
                     font-weight: 700;
                     border: 2px solid #ff00ff;
                     box-shadow: 0 0 25px rgba(255, 0, 255, 0.4);
                     text-transform: uppercase;
                     letter-spacing: 2px;">
            ☁️ Azure Cloud
        </span>
        <span style="background: linear-gradient(135deg, rgba(0, 242, 234, 0.2) 0%, rgba(255, 0, 255, 0.2) 100%); 
                     color: #00f2ea; 
                     padding: 0.8rem 2rem; 
                     border-radius: 30px; 
                     font-family: 'Rajdhani', sans-serif; 
                     font-size: 1rem; 
                     font-weight: 700;
                     border: 2px solid rgba(0, 242, 234, 0.6);
                     box-shadow: 0 0 25px rgba(0, 242, 234, 0.4);
                     text-transform: uppercase;
                     letter-spacing: 2px;">
            📊 Auto-Learning
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR VISIBLE CON BOTÓN TOGGLE
# ==========================================
st.markdown("""
<style>
    /* FORZAR sidebar SIEMPRE VISIBLE */
    section[data-testid="stSidebar"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        position: fixed !important;
        left: 0px !important;
        width: 21rem !important;
        height: 100vh !important;
        z-index: 999 !important;
        transform: translateX(0) !important;
    }
    
    /* Contenido del sidebar visible */
    [data-testid="stSidebarContent"],
    [data-testid="stSidebarUserContent"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    
    /* Botón de colapso nativo de Streamlit - VISIBLE y ESTILIZADO */
    [data-testid="stSidebarCollapseButton"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        position: absolute !important;
        top: 0.5rem !important;
        right: 0.5rem !important;
        z-index: 99999 !important;
    }
    
    [data-testid="stSidebarCollapseButton"] button,
    button[kind="headerNoPadding"] {
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.3), rgba(255, 0, 255, 0.3)) !important;
        border: 2px solid rgba(0, 242, 234, 0.7) !important;
        border-radius: 10px !important;
        padding: 10px !important;
        width: 44px !important;
        height: 44px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0 4px 15px rgba(0, 242, 234, 0.5) !important;
        transition: all 0.2s ease !important;
    }
    
    [data-testid="stSidebarCollapseButton"] button:hover {
        background: linear-gradient(135deg, rgba(0, 242, 234, 0.5), rgba(255, 0, 255, 0.5)) !important;
        transform: scale(1.1) !important;
        box-shadow: 0 6px 20px rgba(0, 242, 234, 0.7) !important;
    }
    
    /* Estilizar el ícono dentro del botón */
    [data-testid="stSidebarCollapseButton"] button span[data-testid="stIconMaterial"] {
        color: #00f2ea !important;
        font-size: 24px !important;
    }
    
    /* AJUSTAR contenido principal - cuando sidebar está visible */
    .main,
    [data-testid="stAppViewContainer"] .main {
        margin-left: 21rem !important;
        transition: margin-left 0.3s ease;
    }
    
    .main .block-container {
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: calc(100vw - 25rem) !important;
    }
    
    /* Cuando el sidebar se colapsa (aunque intentamos prevenirlo) */
    section[data-testid="stSidebar"][aria-expanded="false"] {
        transform: translateX(0) !important;
        left: 0 !important;
    }
</style>

<script>
    // Forzar sidebar SIEMPRE visible
    function forceSidebarVisible() {
        const sidebar = document.querySelector('section[data-testid="stSidebar"]');
        const main = document.querySelector('.main');
        const collapseButton = document.querySelector('[data-testid="stSidebarCollapseButton"]');
        
        if (sidebar) {
            // Forzar sidebar visible en su posición
            sidebar.style.display = 'block';
            sidebar.style.visibility = 'visible';
            sidebar.style.opacity = '1';
            sidebar.style.left = '0px';
            sidebar.style.transform = 'translateX(0)';
            sidebar.style.position = 'fixed';
            sidebar.style.width = '21rem';
            
            // Forzar contenido visible
            const content = sidebar.querySelector('[data-testid="stSidebarContent"]');
            if (content) {
                content.style.display = 'block';
                content.style.visibility = 'visible';
                content.style.opacity = '1';
            }
            
            // Asegurar que el botón de colapso esté visible
            if (collapseButton) {
                collapseButton.style.display = 'flex';
                collapseButton.style.visibility = 'visible';
                collapseButton.style.opacity = '1';
            }
        }
        
        // Ajustar contenido principal
        if (main) {
            main.style.marginLeft = '21rem';
        }
    }
    
    // Ejecutar cada 100ms para mantener sidebar visible
    setInterval(forceSidebarVisible, 100);
    
    // Ejecutar inmediatamente
    setTimeout(forceSidebarVisible, 50);
    
    // Observar cambios y revertirlos
    setTimeout(() => {
        const sidebar = document.querySelector('section[data-testid="stSidebar"]');
        if (sidebar) {
            const observer = new MutationObserver(forceSidebarVisible);
            observer.observe(sidebar, { 
                attributes: true,
                childList: true,
                subtree: true
            });
        }
    }, 500);
    
    console.log('✅ Sidebar forzado a estar SIEMPRE visible');
</script>
""", unsafe_allow_html=True)

# Inicializar estado de sesión
if 'memoria' not in st.session_state:
    st.session_state.memoria = cargar_memoria()

if 'resultados_comparacion' not in st.session_state:
    st.session_state.resultados_comparacion = None

if 'ultimo_documento' not in st.session_state:
    st.session_state.ultimo_documento = None

if 'resultados_batch' not in st.session_state:
    st.session_state.resultados_batch = None

# ============================================
# SIDEBAR - CONFIGURACIÓN Y MÉTRICAS
# ============================================

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h2 style="color: white; font-family: 'Poppins', sans-serif; font-weight: 700; margin-bottom: 0.5rem;">⚙️ PANEL DE CONTROL</h2>
        <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">Configure su experiencia de extracción</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Modo de Selección Inteligente (por defecto)
    st.markdown("""
    <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                border-radius: 12px; padding: 1.2rem; margin-bottom: 1rem;
                box-shadow: 0 8px 20px rgba(17, 153, 142, 0.4);">
        <div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">
            <div style="font-size: 2rem;">🤖</div>
            <div>
                <div style="color: white; font-weight: 700; font-size: 1.1rem;">Modo Inteligente</div>
                <div style="color: rgba(255,255,255,0.9); font-size: 0.8rem;">Selección automática activada</div>
            </div>
        </div>
        <div style="background: rgba(255,255,255,0.2); border-radius: 8px; padding: 0.8rem; margin-top: 0.8rem;">
            <div style="color: rgba(255,255,255,0.95); font-size: 0.85rem; line-height: 1.4;">
                ✨ El sistema analizará tu documento y elegirá automáticamente la mejor estrategia de extracción
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Opciones avanzadas (colapsables y opcionales)
    with st.expander("Configuración Avanzada", expanded=False):
        st.markdown("""
        <div style="background: rgba(255,152,0,0.15); border-radius: 8px; padding: 0.8rem; margin-bottom: 1rem; border-left: 3px solid #ff9800;">
            <div style="color: #ff9800; font-size: 0.85rem; font-weight: 600; margin-bottom: 0.3rem;">⚠️ Solo para usuarios avanzados</div>
            <div style="color: rgba(255, 255, 255, 0.85); font-size: 0.75rem; line-height: 1.4;">
                Cambia la estrategia solo si necesitas forzar un método específico. La selección automática es óptima para el 95% de los casos.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        estrategia = st.selectbox(
            "🎯 Forzar Estrategia Específica:",
            ["AUTO (Recomendado)", "RAPIDO", "BALANCEADO", "PRECISO", "AZURE", "COMPARAR"],
            index=0,
            help="""
            🤖 AUTO: Selección inteligente automática (RECOMENDADO)
            ⚡ RAPIDO: Solo Tesseract - ultrarrápido (1-2s)
            ⚖️ BALANCEADO: Tesseract + PaddleOCR (3-5s)
            🎯 PRECISO: EasyOCR + PaddleOCR - máxima precisión (10-15s)
            ☁️ AZURE: Azure Document Intelligence Cloud (2-4s)
            🔬 COMPARAR: Ejecuta todos y compara resultados
            """
        )
        
        # Limpiar el nombre de la estrategia (quitar " (Recomendado)")
        estrategia = estrategia.split(" ")[0]
        
        # Badges de estrategia
        st.markdown(f"""
        <div style="margin-top: 0.8rem;">
            <div style="background: rgba(102, 126, 234, 0.15); border-radius: 10px; padding: 0.8rem;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #555; font-size: 0.85rem; font-weight: 600;">⏱️ Velocidad:</span>
                    <span style="color: #667eea; font-weight: 700;">{'⚡⚡⚡⚡⚡' if estrategia == 'RAPIDO' else '⚡⚡⚡⚡' if estrategia in ['AUTO', 'AZURE'] else '⚡⚡⚡' if estrategia == 'BALANCEADO' else '⚡⚡'}</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 0.5rem;">
                    <span style="color: #555; font-size: 0.85rem; font-weight: 600;">🎯 Precisión:</span>
                    <span style="color: #667eea; font-weight: 700;">{'⭐⭐⭐⭐⭐' if estrategia in ['PRECISO', 'AZURE'] else '⭐⭐⭐⭐' if estrategia in ['AUTO', 'BALANCEADO'] else '⭐⭐⭐'}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Si no se expandió, usar AUTO por defecto
    if 'estrategia' not in locals():
        estrategia = "AUTO"
    
    st.divider()
    
    # Estado del sistema con diseño moderno
    st.markdown("""
    <h3 style='color: white; font-family: Poppins; font-size: 1.1rem; margin-bottom: 1rem;'>📊 Estado del Sistema</h3>
    """, unsafe_allow_html=True)
    
    # Verificar Azure
    try:
        from config import AZURE_ENDPOINT, AZURE_KEY
        azure_ok = bool(AZURE_ENDPOINT and AZURE_KEY)
    except:
        azure_ok = False
    
    # Métricas del sistema con glassmorphism
    motores = [
        ("Tesseract", True, "⚡ Ultrarrápido"),
        ("PaddleOCR", True, "📊 Tablas"),
        ("EasyOCR", True, "🎯 Preciso"),
        ("Azure AI", azure_ok, "☁️ Cloud")
    ]
    
    for motor, activo, descripcion in motores:
        status_color = "#38ef7d" if activo else "#f5576c"
        status_icon = "✅" if activo else "⚠️"
        status_text = "Operacional" if activo else "No Config"
        
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.15); border-radius: 10px; padding: 0.8rem; margin-bottom: 0.5rem; backdrop-filter: blur(10px); border-left: 4px solid {status_color};">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="color: white; font-weight: 600; font-size: 0.95rem;">{status_icon} {motor}</div>
                    <div style="color: rgba(255,255,255,0.7); font-size: 0.75rem; margin-top: 0.2rem;">{descripcion}</div>
                </div>
                <div style="background: {status_color}; color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.7rem; font-weight: 600;">
                    {status_text}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Auto-aprendizaje con visualización mejorada
    st.markdown("""
    <h3 style='color: white; font-family: Poppins; font-size: 1.1rem; margin-bottom: 1rem;'>🧠 Inteligencia Adaptativa</h3>
    """, unsafe_allow_html=True)
    
    memoria = st.session_state.memoria
    nombres_aprendidos = len(memoria.get('nombres_completos', {}))
    correcciones_totales = sum(
        info.get('apariciones', 0) 
        for info in memoria.get('nombres_completos', {}).values()
    )
    
    # Métricas de aprendizaje con diseño circular
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 15px; padding: 1.2rem; text-align: center; box-shadow: 0 8px 20px rgba(240, 147, 251, 0.4);">
            <div style="font-size: 2.2rem; font-weight: 700; color: white; margin-bottom: 0.3rem;">{nombres_aprendidos}</div>
            <div style="color: rgba(255,255,255,0.9); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Nombres</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); border-radius: 15px; padding: 1.2rem; text-align: center; box-shadow: 0 8px 20px rgba(17, 153, 142, 0.4);">
            <div style="font-size: 2.2rem; font-weight: 700; color: white; margin-bottom: 0.3rem;">{correcciones_totales}</div>
            <div style="color: rgba(255,255,255,0.9); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Correcciones</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Botón de limpiar con diseño moderno
    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    if st.button("🗑️ Resetear Memoria", use_container_width=True, help="Elimina todo el conocimiento aprendido"):
        st.session_state.memoria = {'nombres_completos': {}}
        guardar_memoria(st.session_state.memoria)
        st.success("✅ Memoria reseteada exitosamente")
        st.rerun()
    
    # Footer del sidebar
    st.markdown("""
    <div style="position: absolute; bottom: 1rem; left: 0; right: 0; padding: 0 1rem;">
        <div style="background: rgba(255,255,255,0.1); border-radius: 10px; padding: 1rem; text-align: center; backdrop-filter: blur(10px);">
            <div style="color: white; font-size: 0.75rem; margin-bottom: 0.5rem;">💡 Tip del Día</div>
            <div style="color: rgba(255,255,255,0.8); font-size: 0.7rem; line-height: 1.4;">
                Usa <b>AUTO</b> para dejar que la IA elija la mejor estrategia automáticamente
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# ÁREA PRINCIPAL - CARGA Y PROCESAMIENTO
# ============================================

tab1, tab2, tab3, tab4 = st.tabs([
    "📄 Procesar Documento", 
    "📊 Comparar Métodos", 
    "🧠 Memoria de Aprendizaje", 
    "ℹ️ Ayuda"
])

# ============================================
# TAB 1: PROCESAR DOCUMENTO
# ============================================

with tab1:
    # Header visual mejorado
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); 
                border-radius: 15px; padding: 1.5rem; margin-bottom: 2rem; border-left: 5px solid #667eea;">
        <h2 style="color: #667eea; font-family: 'Poppins', sans-serif; margin: 0; font-weight: 700;">
            📤 Cargar y Procesar Documentos
        </h2>
        <p style="color: #555; margin-top: 0.5rem; margin-bottom: 0;">
            Sube uno o varios documentos para extraer datos automáticamente
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Modo de carga: archivo único, múltiples o carpeta
    st.markdown("""
    <div style="margin-bottom: 1rem; margin-top: 1.5rem;">
        <label style="font-family: 'Poppins', sans-serif; font-weight: 600; color: #ffffff; font-size: 0.95rem;">
            📂 Modo de Carga:
        </label>
    </div>
    """, unsafe_allow_html=True)
    
    modo_carga = st.radio(
        "Modo de carga:",
        ["📄 Archivo Único", "📷 Capturar Foto", "📁 Carpeta Completa"],
        horizontal=True,
        label_visibility="collapsed",
        help="""
        📄 Archivo Único: Procesa un solo documento
        📷 Capturar Foto: Usa la cámara de tu dispositivo (ideal para móviles)
        📁 Carpeta Completa: Selecciona múltiples archivos de una carpeta
        """
    )
    
    # Selector de tipo de archivo con diseño visual - OCULTO
    # st.markdown("""
    # <div style="margin-bottom: 1rem; margin-top: 1.5rem;">
    #     <label style="font-family: 'Poppins', sans-serif; font-weight: 600; color: #ffffff; font-size: 0.95rem;">
    #         🎯 Tipo de Archivos:
    #     </label>
    # </div>
    # """, unsafe_allow_html=True)
    
    # tipo_archivo = st.radio(
    #     "Tipo de archivo:",
    #     ["Imagen (JPG, PNG)", "PDF"],
    #     horizontal=True,
    #     label_visibility="collapsed"
    # )
    
    # Auto-detectar tipo de archivo (siempre imagen por defecto)
    tipo_archivo = "Imagen (JPG, PNG)"
    
    # File uploader con diseño mejorado según modo de carga
    archivos_cargados = []
    foto_camara = None
    
    if modo_carga == "📷 Capturar Foto":
        # Modo cámara: captura directa desde el dispositivo
        st.markdown("""
        <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                    border-radius: 15px; padding: 1.5rem; margin: 1rem 0; color: white;">
            <div style="font-size: 2rem; text-align: center; margin-bottom: 0.5rem;">📷</div>
            <h3 style="color: white; text-align: center; margin-bottom: 0.5rem;">Captura de Foto</h3>
            <p style="text-align: center; margin: 0; font-size: 0.95rem; opacity: 0.9;">
                📱 Ideal para móviles, tablets y PCs con cámara<br>
                ✨ Captura documentos directamente sin necesidad de archivos
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        foto_camara = st.camera_input(
            "📸 Toma una foto del documento",
            help="🎯 Asegúrate de tener buena iluminación y que el documento esté completo en el encuadre"
        )
        
        if foto_camara:
            # Convertir la captura a formato compatible
            from io import BytesIO
            archivos_cargados = [foto_camara]
            tipo_archivo = "Imagen (JPG, PNG)"  # Las capturas son siempre imágenes
    
    elif modo_carga == "📄 Archivo Único":
        # Modo tradicional: un solo archivo
        if tipo_archivo == "Imagen (JPG, PNG)":
            archivo = st.file_uploader(
                "Arrastra o selecciona una imagen",
                type=["jpg", "jpeg", "png"],
                help="✨ Formatos soportados: JPG, JPEG, PNG | Tamaño máximo: 200MB"
            )
        else:
            archivo = st.file_uploader(
                "Arrastra o selecciona un PDF",
                type=["pdf"],
                help="📄 El PDF será convertido automáticamente a imagen para procesamiento"
            )
        
        if archivo:
            archivos_cargados = [archivo]
    
    else:  # Carpeta Completa
        # Modo carpeta: varios archivos a la vez
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 15px; padding: 1.5rem; margin: 1rem 0; color: white;">
            <div style="font-size: 2rem; text-align: center; margin-bottom: 0.5rem;">📁</div>
            <h3 style="color: white; text-align: center; margin-bottom: 0.5rem;">Carpeta Completa</h3>
            <p style="text-align: center; margin: 0; font-size: 0.95rem; opacity: 0.9;">
                💡 Selecciona múltiples archivos de una carpeta<br>
                ⚡ Usa <strong>Ctrl+Click</strong> o <strong>Ctrl+A</strong> para seleccionar varios
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if tipo_archivo == "Imagen (JPG, PNG)":
            archivos = st.file_uploader(
                "Arrastra o selecciona múltiples imágenes",
                type=["jpg", "jpeg", "png"],
                accept_multiple_files=True,
                help="✨ Puedes seleccionar varios archivos a la vez | Formatos: JPG, JPEG, PNG"
            )
        else:
            archivos = st.file_uploader(
                "Arrastra o selecciona múltiples PDFs",
                type=["pdf"],
                accept_multiple_files=True,
                help="📄 Puedes seleccionar varios archivos PDF a la vez"
            )
        
        if archivos:
            archivos_cargados = archivos
    
    # Mostrar resumen de archivos cargados
    if archivos_cargados:
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        # Resumen visual
        total_archivos = len(archivos_cargados)
        tamaño_total = sum(f.size for f in archivos_cargados) / (1024 * 1024)  # MB
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        border-radius: 12px; padding: 1.2rem; text-align: center;
                        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);">
                <div style="color: rgba(255,255,255,0.9); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Archivos</div>
                <div style="color: white; font-size: 2rem; font-weight: 700; margin-top: 0.3rem;">{total_archivos}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                        border-radius: 12px; padding: 1.2rem; text-align: center;
                        box-shadow: 0 8px 20px rgba(17, 153, 142, 0.3);">
                <div style="color: rgba(255,255,255,0.9); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Tamaño Total</div>
                <div style="color: white; font-size: 2rem; font-weight: 700; margin-top: 0.3rem;">{tamaño_total:.1f}MB</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                        border-radius: 12px; padding: 1.2rem; text-align: center;
                        box-shadow: 0 8px 20px rgba(240, 147, 251, 0.3);">
                <div style="color: rgba(255,255,255,0.9); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Tipo</div>
                <div style="color: white; font-size: 2rem; font-weight: 700; margin-top: 0.3rem;">{tipo_archivo.split()[0]}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        # Mostrar lista de archivos si son más de 1
        if total_archivos > 1:
            with st.expander(f"📋 Ver lista completa de {total_archivos} archivos", expanded=False):
                for i, archivo in enumerate(archivos_cargados, 1):
                    tamaño = archivo.size / 1024  # KB
                    st.markdown(f"""
                    <div style="background: rgba(102, 126, 234, 0.05); border-radius: 8px; padding: 0.8rem; margin-bottom: 0.5rem; border-left: 3px solid #667eea;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <span style="color: #667eea; font-weight: 600;">{i}.</span>
                                <span style="color: rgba(255, 255, 255, 0.95); font-weight: 500; margin-left: 0.5rem;">{archivo.name}</span>
                            </div>
                            <span style="color: rgba(255, 255, 255, 0.7); font-size: 0.85rem;">{tamaño:.1f} KB</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Vista previa del primer archivo
        st.markdown("""
        <div style="margin-bottom: 1rem; margin-top: 2rem;">
            <h3 style="font-family: 'Poppins', sans-serif; color: #667eea; font-weight: 600; font-size: 1.1rem;">
                🖼️ Vista Previa{' del Primer Archivo' if total_archivos > 1 else ''}
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Mostrar vista previa del primer archivo
        col_img, col_info = st.columns([2, 1])
        
        archivo_preview = archivos_cargados[0]
        
        with col_img:
            if tipo_archivo == "Imagen (JPG, PNG)":
                imagen = Image.open(archivo_preview)
                st.image(imagen, caption=archivo_preview.name, use_container_width=True)
            else:
                st.markdown("""
                <div class="info-box" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                            color: white; padding: 2rem; border-radius: 15px; text-align: center;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">📄</div>
                    <div style="font-size: 1.2rem; font-weight: 600;">PDF Cargado Correctamente</div>
                    <div style="font-size: 0.9rem; margin-top: 0.5rem; opacity: 0.9;">
                        Se procesará la primera página automáticamente
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col_info:
            st.markdown("""
            <div style="margin-bottom: 1rem;">
                <h3 style="font-family: 'Poppins', sans-serif; color: #667eea; font-weight: 600; font-size: 1.1rem;">
                    📋 Información
                </h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Tarjeta de información con glassmorphism
            tamaño_kb = archivo_preview.size / 1024
            tamaño_str = f"{tamaño_kb:.2f} KB" if tamaño_kb < 1024 else f"{tamaño_kb/1024:.2f} MB"
            
            st.markdown(f"""
            <div style="background: rgba(102, 126, 234, 0.1); border-radius: 12px; padding: 1.2rem; 
                        backdrop-filter: blur(10px); border: 1px solid rgba(102, 126, 234, 0.2);">
                <div style="margin-bottom: 0.8rem;">
                    <div style="color: rgba(255, 255, 255, 0.6); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Nombre</div>
                    <div style="color: rgba(255, 255, 255, 0.95); font-weight: 600; margin-top: 0.3rem; word-break: break-all;">{archivo_preview.name}</div>
                </div>
                <div style="margin-bottom: 0.8rem;">
                    <div style="color: rgba(255, 255, 255, 0.6); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Tipo</div>
                    <div style="color: rgba(255, 255, 255, 0.95); font-weight: 600; margin-top: 0.3rem;">{archivo_preview.type}</div>
                </div>
                <div>
                    <div style="color: rgba(255, 255, 255, 0.6); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Tamaño</div>
                    <div style="color: rgba(255, 255, 255, 0.95); font-weight: 600; margin-top: 0.3rem;">{tamaño_str}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Badge de estrategia seleccionada
            if estrategia == "AUTO":
                badge_color = "linear-gradient(135deg, #11998e 0%, #38ef7d 100%)"
                badge_shadow = "rgba(17, 153, 142, 0.3)"
                badge_icon = "🤖"
                badge_title = "MODO AUTOMÁTICO"
                badge_subtitle = "El sistema elegirá la mejor estrategia"
            else:
                badge_color = "linear-gradient(135deg, #ff9800 0%, #ff5722 100%)"
                badge_shadow = "rgba(255, 152, 0, 0.3)"
                badge_icon = "⚙️"
                badge_title = f"FORZADO: {estrategia}"
                badge_subtitle = "Estrategia manual seleccionada"
            
            st.markdown(f"""
            <div style="margin-top: 1.5rem; background: {badge_color}; 
                        border-radius: 12px; padding: 1rem; text-align: center; box-shadow: 0 8px 20px {badge_shadow};">
                <div style="font-size: 1.5rem; margin-bottom: 0.3rem;">{badge_icon}</div>
                <div style="color: white; font-size: 0.75rem; opacity: 0.9; margin-bottom: 0.3rem; text-transform: uppercase; letter-spacing: 1px;">{badge_subtitle}</div>
                <div style="color: white; font-size: 1.1rem; font-weight: 700;">{badge_title}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        # Botón de procesamiento con diseño impactante
        texto_boton = f"🚀 PROCESAR {total_archivos} ARCHIVO{'S' if total_archivos > 1 else ''}"
        col_btn = st.columns([1, 2, 1])
        with col_btn[1]:
            if st.button(texto_boton, type="primary", use_container_width=True):
                
                # Inicializar variables para procesamiento batch
                resultados_batch = []
                total_procesados = 0
                total_errores = 0
                inicio_total = time.time()
                
                # Barra de progreso para múltiples archivos
                if total_archivos > 1:
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                
                # Procesar cada archivo
                for idx, archivo in enumerate(archivos_cargados, 1):
                    try:
                        # Actualizar progreso
                        if total_archivos > 1:
                            progreso = idx / total_archivos
                            progress_bar.progress(progreso)
                            status_text.markdown(f"""
                            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                                        border-radius: 12px; padding: 1.5rem; text-align: center; margin: 1rem 0;
                                        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);">
                                <div style="color: white; font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem;">
                                    ⚙️ Procesando: {archivo.name}
                                </div>
                                <div style="color: rgba(255,255,255,0.9); font-size: 0.9rem;">
                                    Archivo {idx} de {total_archivos} | Estrategia: <strong>{estrategia}</strong>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            # Mensaje para archivo único
                            st.markdown(f"""
                            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                                        border-radius: 15px; padding: 2rem; text-align: center; 
                                        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
                                        animation: pulse 2s ease-in-out infinite;">
                                <div style="font-size: 2.5rem; margin-bottom: 1rem;">⚙️</div>
                                <div style="color: white; font-size: 1.3rem; font-weight: 700; margin-bottom: 0.5rem;">
                                    Procesando Documento
                                </div>
                                <div style="color: rgba(255,255,255,0.9); font-size: 0.95rem;">
                                    Estrategia: <strong>{estrategia}</strong> | Por favor espere...
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        inicio_archivo = time.time()
                        
                        # Procesar según tipo
                        if tipo_archivo == "Imagen (JPG, PNG)":
                            imagen = Image.open(archivo)
                        else:
                            # Convertir PDF a imagen
                            from pdf2image import convert_from_bytes
                            imagenes = convert_from_bytes(
                                archivo.read(),
                                dpi=200,
                                first_page=1,
                                last_page=1
                            )
                            imagen = imagenes[0]
                        
                        # Extraer datos
                        if estrategia == "COMPARAR":
                            resultado_comparacion = extraer_documento(imagen, comparar=True)
                            resultados_batch.append({
                                'nombre': archivo.name,
                                'tipo': 'comparacion',
                                'datos': resultado_comparacion,
                                'tiempo': time.time() - inicio_archivo
                            })
                        else:
                            datos, tiempo = extraer_documento(imagen, estrategia=estrategia)
                            resultados_batch.append({
                                'nombre': archivo.name,
                                'tipo': 'extraccion',
                                'datos': datos,
                                'tiempo': tiempo
                            })
                        
                        total_procesados += 1
                        
                    except Exception as e:
                        total_errores += 1
                        resultados_batch.append({
                            'nombre': archivo.name,
                            'tipo': 'error',
                            'error': str(e),
                            'tiempo': time.time() - inicio_archivo
                        })
                
                # Limpiar progreso
                if total_archivos > 1:
                    progress_bar.empty()
                    status_text.empty()
                
                tiempo_total = time.time() - inicio_total
                
                # Guardar resultados en session state
                if total_archivos == 1 and resultados_batch[0]['tipo'] == 'extraccion':
                    # Modo individual: compatible con la vista existente
                    st.session_state.ultimo_documento = (resultados_batch[0]['datos'], resultados_batch[0]['tiempo'])
                    st.session_state.resultados_comparacion = None
                elif total_archivos == 1 and resultados_batch[0]['tipo'] == 'comparacion':
                    st.session_state.resultados_comparacion = resultados_batch[0]['datos']
                    st.session_state.ultimo_documento = None
                else:
                    # Modo batch: guardar todos los resultados
                    st.session_state.resultados_batch = resultados_batch
                    st.session_state.ultimo_documento = None
                    st.session_state.resultados_comparacion = None
                
                # Mensaje de éxito con diseño impactante
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                            border-radius: 15px; padding: 2rem; margin-top: 2rem;
                            box-shadow: 0 10px 30px rgba(17, 153, 142, 0.4);
                            animation: slideInUp 0.5s ease;">
                    <div style="text-align: center; margin-bottom: 1.5rem;">
                        <div style="font-size: 3rem; margin-bottom: 0.5rem;">✅</div>
                        <h2 style="color: white; font-family: 'Poppins', sans-serif; margin: 0; font-weight: 700;">
                            ¡Procesamiento Completado!
                        </h2>
                    </div>
                    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 1rem;">
                        <div style="background: rgba(255,255,255,0.2); border-radius: 10px; padding: 1rem; flex: 1; min-width: 120px; text-align: center;">
                            <div style="color: rgba(255,255,255,0.9); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Archivos</div>
                            <div style="color: white; font-size: 1.6rem; font-weight: 700; margin-top: 0.3rem;">{total_archivos}</div>
                        </div>
                        <div style="background: rgba(255,255,255,0.2); border-radius: 10px; padding: 1rem; flex: 1; min-width: 120px; text-align: center;">
                            <div style="color: rgba(255,255,255,0.9); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Exitosos</div>
                            <div style="color: white; font-size: 1.6rem; font-weight: 700; margin-top: 0.3rem;">{total_procesados}</div>
                        </div>
                        <div style="background: rgba(255,255,255,0.2); border-radius: 10px; padding: 1rem; flex: 1; min-width: 120px; text-align: center;">
                            <div style="color: rgba(255,255,255,0.9); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Errores</div>
                            <div style="color: white; font-size: 1.6rem; font-weight: 700; margin-top: 0.3rem;">{total_errores}</div>
                        </div>
                        <div style="background: rgba(255,255,255,0.2); border-radius: 10px; padding: 1rem; flex: 1; min-width: 120px; text-align: center;">
                            <div style="color: rgba(255,255,255,0.9); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Tiempo Total</div>
                            <div style="color: white; font-size: 1.6rem; font-weight: 700; margin-top: 0.3rem;">{tiempo_total:.1f}s</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Mostrar resultados batch (múltiples archivos)
        if 'resultados_batch' in st.session_state and st.session_state.resultados_batch:
            st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); 
                        border-radius: 15px; padding: 1.5rem; margin-bottom: 2rem; border-left: 5px solid #667eea;">
                <h2 style="color: #667eea; font-family: 'Poppins', sans-serif; margin: 0; font-weight: 700;">
                    📊 Resultados de Procesamiento Batch
                </h2>
                <p style="color: #555; margin-top: 0.5rem; margin-bottom: 0;">
                    Resumen de extracciones para todos los archivos procesados
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Mostrar cada resultado
            for idx, resultado in enumerate(st.session_state.resultados_batch, 1):
                nombre = resultado['nombre']
                tipo = resultado['tipo']
                tiempo_archivo = resultado.get('tiempo', 0)
                
                if tipo == 'error':
                    # Mostrar error
                    st.markdown(f"""
                    <div style="background: rgba(245, 87, 108, 0.1); border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem; border-left: 4px solid #f5576c;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                            <div>
                                <span style="color: #f5576c; font-weight: 700; font-size: 1.1rem;">❌ {idx}. {nombre}</span>
                            </div>
                            <span style="color: rgba(255, 255, 255, 0.7); font-size: 0.85rem;">{tiempo_archivo:.2f}s</span>
                        </div>
                        <div style="background: rgba(0,0,0,0.3); border-radius: 8px; padding: 1rem; margin-top: 0.8rem;">
                            <div style="color: rgba(255, 255, 255, 0.9); font-size: 0.9rem; font-family: monospace;">{resultado['error']}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    # Mostrar extracción exitosa
                    with st.expander(f"✅ {idx}. {nombre} ({tiempo_archivo:.2f}s)", expanded=idx==1):
                        datos = resultado['datos']
                        
                        # Filtrar campos normales
                        campos_normales_dict = {k: v for k, v in datos.items() if not k.startswith('_')}
                        
                        if campos_normales_dict:
                            df = pd.DataFrame(
                                list(campos_normales_dict.items()),
                                columns=['Campo', 'Valor']
                            )
                            st.dataframe(df, use_container_width=True, height=300)
                            
                            # Botón de descarga individual
                            csv = df.to_csv(index=False).encode('utf-8')
                            st.download_button(
                                label=f"📥 Descargar {nombre}.csv",
                                data=csv,
                                file_name=f"{nombre}_extraccion.csv",
                                mime="text/csv",
                                key=f"download_{idx}"
                            )
            
            # Descarga consolidada de todos los resultados
            st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
            
            if st.button("📦 Descargar Todos los Resultados (Excel)", use_container_width=True):
                # Crear Excel con múltiples hojas
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    for idx, resultado in enumerate(st.session_state.resultados_batch, 1):
                        if resultado['tipo'] != 'error':
                            datos = resultado['datos']
                            campos_normales_dict = {k: v for k, v in datos.items() if not k.startswith('_')}
                            
                            if campos_normales_dict:
                                df = pd.DataFrame(
                                    list(campos_normales_dict.items()),
                                    columns=['Campo', 'Valor']
                                )
                                # Nombre de hoja truncado a 31 caracteres (límite de Excel)
                                nombre_hoja = f"Archivo_{idx}"[:31]
                                df.to_excel(writer, index=False, sheet_name=nombre_hoja)
                
                st.download_button(
                    label="📥 Descargar Excel Consolidado",
                    data=buffer.getvalue(),
                    file_name=f"extraccion_batch_{len(st.session_state.resultados_batch)}_archivos.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        
        # Mostrar resultados individuales (archivo único)
        elif st.session_state.ultimo_documento:
            datos, tiempo = st.session_state.ultimo_documento
            
            st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)
            
            # Header de resultados con diseño moderno
            st.markdown("""
            <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); 
                        border-radius: 15px; padding: 1.5rem; margin-bottom: 2rem; border-left: 5px solid #667eea;">
                <h2 style="color: #667eea; font-family: 'Poppins', sans-serif; margin: 0; font-weight: 700;">
                    📊 Resultados de Extracción
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Métricas con diseño visual impactante
            campos_totales = len(datos)
            campos_auto = len([k for k in datos.keys() if k.startswith('Auto_')])
            campos_normales = campos_totales - campos_auto
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                            border-radius: 15px; padding: 1.5rem; text-align: center;
                            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
                            transition: transform 0.3s ease;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">⏱️</div>
                    <div style="color: white; font-size: 2rem; font-weight: 700; margin-bottom: 0.3rem;">{tiempo:.2f}s</div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Tiempo</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                            border-radius: 15px; padding: 1.5rem; text-align: center;
                            box-shadow: 0 8px 20px rgba(17, 153, 142, 0.4);
                            transition: transform 0.3s ease;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📝</div>
                    <div style="color: white; font-size: 2rem; font-weight: 700; margin-bottom: 0.3rem;">{campos_normales}</div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Campos Extraídos</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                            border-radius: 15px; padding: 1.5rem; text-align: center;
                            box-shadow: 0 8px 20px rgba(240, 147, 251, 0.4);
                            transition: transform 0.3s ease;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🤖</div>
                    <div style="color: white; font-size: 2rem; font-weight: 700; margin-bottom: 0.3rem;">{campos_auto}</div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Auto-Detectados</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
            
            # Tabs para diferentes vistas
            tab_datos, tab_tabla, tab_json = st.tabs(["📋 Datos Extraídos", "📊 Tablas", "💾 JSON"])
            
            with tab_datos:
                # Filtrar campos normales
                campos_normales_dict = {k: v for k, v in datos.items() if not k.startswith('_')}
                
                if campos_normales_dict:
                    st.markdown("""
                    <div style="margin-bottom: 1rem;">
                        <h3 style="font-family: 'Poppins', sans-serif; color: #667eea; font-weight: 600; font-size: 1.1rem;">
                            📋 Información Extraída del Documento
                        </h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    df = pd.DataFrame(
                        list(campos_normales_dict.items()),
                        columns=['Campo', 'Valor']
                    )
                    st.dataframe(df, use_container_width=True, height=400)
                    
                    # Botón de descarga CSV con diseño mejorado
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 Descargar CSV",
                        data=csv,
                        file_name=f"extraccion_{estrategia.lower()}.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
                else:
                    st.markdown("""
                    <div style="background: rgba(245, 87, 108, 0.1); border-radius: 12px; padding: 2rem; text-align: center; border-left: 4px solid #f5576c;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚠️</div>
                        <div style="color: #f5576c; font-weight: 600; font-size: 1.1rem;">No se extrajeron campos de datos</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            with tab_tabla:
                # Mostrar tablas si existen
                if '_filas' in datos and datos['_filas']:
                    st.markdown("""
                    <div style="margin-bottom: 1rem;">
                        <h3 style="font-family: 'Poppins', sans-serif; color: #667eea; font-weight: 600; font-size: 1.1rem;">
                            📊 Tabla Extraída del Documento
                        </h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    filas = datos['_filas']
                    if filas:
                        # Convertir a DataFrame
                        df_tabla = pd.DataFrame(filas)
                        st.dataframe(df_tabla, use_container_width=True, height=400)
                        
                        # Botón de descarga Excel
                        buffer = io.BytesIO()
                        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                            df_tabla.to_excel(writer, index=False, sheet_name='Tabla Extraída')
                        
                        st.download_button(
                            label="📥 Descargar Excel",
                            data=buffer.getvalue(),
                            file_name=f"tabla_{estrategia.lower()}.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            use_container_width=True
                        )
                    else:
                        st.info("La tabla está vacía.")
                        
                elif '_tablas_azure' in datos:
                    st.markdown("""
                    <div style="margin-bottom: 1rem;">
                        <h3 style="font-family: 'Poppins', sans-serif; color: #667eea; font-weight: 600; font-size: 1.1rem;">
                            ☁️ Tablas Extraídas con Azure Document Intelligence
                        </h3>
                    </div>
                    """, unsafe_allow_html=True)
                    for i, tabla in enumerate(datos['_tablas_azure']):
                        st.write(f"**Tabla {i+1}:**")
                        df_tabla = pd.DataFrame(tabla)
                        st.dataframe(df_tabla, use_container_width=True)
                else:
                    st.info("No se detectaron tablas en el documento.")
            
            with tab_json:
                st.subheader("💾 Datos en Formato JSON")
                st.json(datos)
                
                # Botón de descarga JSON
                json_str = json.dumps(datos, indent=2, ensure_ascii=False)
                st.download_button(
                    label="📥 Descargar JSON",
                    data=json_str,
                    file_name=f"extraccion_{estrategia.lower()}.json",
                    mime="application/json"
                )

# ============================================
# TAB 2: COMPARAR MÉTODOS
# ============================================

with tab2:
    st.header("📊 Comparación de Métodos")
    
    if st.session_state.resultados_comparacion:
        resultados = st.session_state.resultados_comparacion
        
        # Tabla comparativa
        st.subheader("⚡ Rendimiento Comparativo")
        
        resumen = []
        for metodo, (datos, tiempo) in resultados.items():
            campos = len([k for k in datos.keys() if not k.startswith('_')])
            resumen.append({
                'Método': metodo.upper(),
                'Tiempo (seg)': round(tiempo, 2),
                'Campos Extraídos': campos,
                'Eficiencia': round(campos / tiempo if tiempo > 0 else 0, 2)
            })
        
        df_resumen = pd.DataFrame(resumen)
        
        # Destacar el más rápido y el que extrajo más campos
        def highlight_max(s):
            if s.name == 'Campos Extraídos':
                is_max = s == s.max()
                return ['background-color: rgba(0, 242, 234, 0.3); color: #ffffff; font-weight: 700' if v else '' for v in is_max]
            elif s.name == 'Tiempo (seg)':
                is_min = s == s.min()
                return ['background-color: rgba(0, 242, 234, 0.3); color: #ffffff; font-weight: 700' if v else '' for v in is_min]
            return ['' for _ in s]
        
        st.dataframe(
            df_resumen.style.apply(highlight_max),
            use_container_width=True,
            hide_index=True
        )
        
        # Gráfico de barras
        st.subheader("📈 Visualización")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.bar_chart(df_resumen.set_index('Método')['Tiempo (seg)'])
            st.caption("⏱️ Tiempo de Procesamiento")
        
        with col2:
            st.bar_chart(df_resumen.set_index('Método')['Campos Extraídos'])
            st.caption("📝 Campos Extraídos")
        
        # Detalles por método
        st.divider()
        st.subheader("🔍 Detalles por Método")
        
        metodo_seleccionado = st.selectbox(
            "Selecciona un método para ver detalles:",
            list(resultados.keys())
        )
        
        if metodo_seleccionado:
            datos, tiempo = resultados[metodo_seleccionado]
            
            st.write(f"**Método:** {metodo_seleccionado.upper()}")
            st.write(f"**Tiempo:** {tiempo:.2f} segundos")
            
            # Mostrar datos
            campos_dict = {k: v for k, v in datos.items() if not k.startswith('_')}
            if campos_dict:
                df = pd.DataFrame(
                    list(campos_dict.items()),
                    columns=['Campo', 'Valor']
                )
                st.dataframe(df, use_container_width=True, height=300)
        
        # Exportar comparación
        st.divider()
        if st.button("📥 Exportar Comparación a Excel", type="primary"):
            try:
                exportar_comparacion_excel(resultados, "comparacion_metodos.xlsx")
                st.success("✅ Comparación exportada a: comparacion_metodos.xlsx")
                
                # Permitir descarga
                with open("comparacion_metodos.xlsx", "rb") as f:
                    st.download_button(
                        label="📥 Descargar Archivo",
                        data=f,
                        file_name="comparacion_metodos.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
            except Exception as e:
                st.error(f"❌ Error exportando: {e}")
    
    else:
        st.info("ℹ️ No hay resultados de comparación. Usa la estrategia 'COMPARAR' en la pestaña anterior.")

# ============================================
# TAB 3: MEMORIA DE APRENDIZAJE
# ============================================

with tab3:
    st.header("🧠 Sistema de Auto-Aprendizaje")
    
    memoria = st.session_state.memoria
    nombres = memoria.get('nombres_completos', {})
    
    if nombres:
        st.success(f"✅ Se han aprendido **{len(nombres)}** nombres únicos")
        
        # Tabla de nombres aprendidos
        datos_nombres = []
        for variante, info in nombres.items():
            datos_nombres.append({
                'Variante Original': variante,
                'Nombre Corregido': info.get('nombre_correcto', ''),
                'Apariciones': info.get('apariciones', 0),
                'Última Fecha': info.get('ultima_actualizacion', 'N/A')
            })
        
        df_nombres = pd.DataFrame(datos_nombres)
        df_nombres = df_nombres.sort_values('Apariciones', ascending=False)
        
        st.dataframe(df_nombres, use_container_width=True, height=400)
        
        # Estadísticas
        st.divider()
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Nombres", len(nombres))
        with col2:
            total_apariciones = sum(info.get('apariciones', 0) for info in nombres.values())
            st.metric("Total Correcciones", total_apariciones)
        with col3:
            promedio = total_apariciones / len(nombres) if nombres else 0
            st.metric("Promedio Uso", f"{promedio:.1f}")
        
        # Exportar memoria
        if st.button("📥 Exportar Memoria a JSON"):
            json_str = json.dumps(memoria, indent=2, ensure_ascii=False)
            st.download_button(
                label="📥 Descargar memoria_aprendizaje.json",
                data=json_str,
                file_name="memoria_aprendizaje.json",
                mime="application/json"
            )
    else:
        st.info("ℹ️ Aún no se han aprendido nombres. Procesa documentos y aplica correcciones para entrenar el sistema.")

# ============================================
# TAB 4: AYUDA
# ============================================

with tab4:
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); 
                border-radius: 15px; padding: 1.5rem; margin-bottom: 2rem; border-left: 5px solid #667eea;">
        <h2 style="color: #667eea; font-family: 'Poppins', sans-serif; margin: 0; font-weight: 700;">
            ℹ️ Guía Rápida de Uso
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## 🚀 Inicio Rápido
    
    ### ¡Es muy simple!
    
    1. **Arrastra o selecciona tu documento** (PDF o imagen)
    2. **Haz clic en "EXTRAER DATOS"** 
    3. **¡Listo!** El sistema automáticamente:
       - Analiza tu documento
       - Selecciona la mejor estrategia de extracción
       - Extrae todos los datos
       - Te muestra los resultados
    
    **No necesitas configurar nada.** El modo automático inteligente está activado por defecto.
    
    ---
    
    ## 🤖 Modo Automático Inteligente (Por Defecto)
    
    El sistema usa IA para analizar tu documento y seleccionar automáticamente la mejor estrategia:
    
    - **📊 Carteras de clientes / Tablas complejas** → PaddleOCR (especializado en tablas)
    - **💊 Fórmulas médicas / Recetas** → Tesseract (rápido y preciso para texto)
    - **📄 Documentos complejos** → Azure Document Intelligence o EasyOCR
    - **📝 Documentos estándar** → Modo balanceado (texto + tablas)
    
    **✨ En el 95% de los casos, no necesitas cambiar nada.** El sistema elegirá por ti.
    
    ---
    
    ## ⚙️ Configuración Avanzada (Opcional)
    
    Si eres un usuario avanzado y quieres **forzar manualmente** una estrategia específica:
    
    1. Ve al **Panel de Control** (sidebar izquierdo)
    2. Expande **"⚙️ Configuración Avanzada (Opcional)"**
    3. Selecciona la estrategia que prefieras
    
    ### Estrategias Disponibles:
    
    ### 1️⃣ AUTO (Recomendado - Por Defecto) 🌟
    - 🤖 Selección inteligente automática basada en IA
    - ✅ **Óptimo para todos los casos**
    - ⚡ Velocidad adaptativa (1-10s según documento)
    - 💡 **No requiere conocimiento técnico**
    
    ### 2️⃣ RAPIDO ⚡
    - Usa solo Tesseract OCR
    - ⚡ Máxima velocidad (1-2 segundos)
    - ⚠️ Menos preciso en tablas complejas
    - 💡 Ideal para: Facturas simples, recibos, formularios básicos
    
    ### 3️⃣ BALANCEADO ⚖️
    - Tesseract para texto + PaddleOCR para tablas
    - ⚡ Rápido-Medio (3-5 segundos)
    - ✅ Buena precisión general
    - 💡 Ideal para: Mayoría de documentos con texto y tablas
    
    ### 4️⃣ PRECISO 🎯
    - EasyOCR + PaddleOCR
    - 🐌 Más lento (10-15 segundos)
    - ⭐ Máxima precisión local
    - 💡 Ideal para: Documentos con texto difícil, baja calidad de escaneo
    
    ### 5️⃣ AZURE
    - Azure Document Intelligence (Cloud)
    - ⚡ Rápido (2-4 segundos)
    - ⭐⭐⭐ Precisión excepcional
    - 💰 Requiere credenciales ($1.50 por 1000 páginas, 500 gratis/mes)
    - 💡 Ideal para: Producción, documentos críticos, tablas muy complejas
    
    ### 6️⃣ COMPARAR
    - Ejecuta TODOS los métodos disponibles
    - 🕐 Más lento (suma de todos)
    - 📊 Permite comparar resultados
    - 💡 Ideal para: Evaluar calidad, decidir mejor método, desarrollo
    
    ---
    
    ## 🧠 Auto-Aprendizaje
    
    El sistema aprende automáticamente de tus correcciones:
    1. Extrae datos de un documento
    2. Si encuentras errores en nombres, corrígelos manualmente
    3. El sistema guarda la corrección en `memoria_aprendizaje.json`
    4. En futuras extracciones, aplicará automáticamente la corrección
    
    ### Ejemplo:
    - **OCR lee:** "JUAN PEREZ GOMFZ" (error en apellido)
    - **Tú corriges:** "JUAN PEREZ GOMEZ"
    - **Sistema aprende:** Próxima vez que vea "GOMFZ" → auto-corregirá a "GOMEZ"
    
    ---
    
    ## 📊 Exportación
    
    Los datos se pueden exportar en múltiples formatos:
    - **CSV** → Importar en Excel, Google Sheets
    - **Excel (XLSX)** → Tablas formateadas, múltiples hojas
    - **JSON** → Integración con APIs, bases de datos
    
    ---
    
    ## 🔐 Seguridad
    
    - Las credenciales de Azure se guardan en `config.py` (gitignored)
    - Los datos extraídos NO se envían a servidores externos (excepto Azure si lo usas)
    - La memoria de aprendizaje se guarda localmente
    
    ---
    
    ## ⚡ Recomendaciones de Uso
    
    ### 🌟 Para la mayoría de usuarios:
    **Deja el modo AUTO activado** (configuración por defecto). El sistema se encargará de todo.
    
    ### 🔧 Para usuarios avanzados:
    
    1. **Si necesitas velocidad máxima a toda costa:** Fuerza RAPIDO (pero perderás precisión en tablas)
    2. **Si tienes credenciales de Azure:** Fuerza AZURE para máxima calidad cloud
    3. **Si quieres comparar diferentes motores:** Usa COMPARAR (toma más tiempo pero genera informe completo)
    4. **Si trabajas offline sin internet:** Evita AZURE, usa AUTO o PRECISO
    
    ### 💡 Consejo del Experto:
    > **El 95% de los usuarios debería usar AUTO** (por defecto). Solo cambia la estrategia si tienes un caso de uso muy específico o estás haciendo pruebas técnicas.
    
    ---
    
    ## 🆘 Solución de Problemas
    
    ### "Azure no está disponible"
    - **Solución:** Configura credenciales en `config.py` con tu cuenta de Azure Portal
    - **O mejor:** Deja el modo AUTO activado, el sistema usará otros motores automáticamente
    
    ### "Extracción muy lenta"
    - **Causa:** Probablemente forzaste estrategia PRECISO o COMPARAR
    - **Solución:** Vuelve al modo AUTO (el sistema equilibrará velocidad y precisión)
    - **O:** Si necesitas velocidad extrema, fuerza RAPIDO
    
    ### "Faltan campos en la extracción"
    - **Solución:** El modo AUTO debería detectar esto automáticamente
    - **Si persiste:** Prueba forzar PRECISO o AZURE manualmente
    - **Tip:** Verifica la calidad de la imagen (mínimo 150 DPI recomendado)
    
    ### "Tabla mal extraída"
    - **Solución:** El modo AUTO debería usar PaddleOCR automáticamente para tablas
    - **Si falla:** Fuerza BALANCEADO o PRECISO (ambos usan PaddleOCR)
    - **Tip:** Asegúrate que la tabla tenga bordes visibles o separación clara de columnas
    
    ### "No sé qué estrategia usar"
    - **Respuesta simple:** ¡No hagas nada! El modo AUTO (por defecto) elegirá por ti 🤖
    """)

    
    st.divider()
    
    st.markdown("""
    ## 📚 Recursos Adicionales
    
    - **Azure Setup:** Lee `README_AZURE.md` para configurar credenciales
    - **GitHub:** Consulta `GUIA_GITHUB.md` para subir el proyecto
    - **Ejemplos:** Revisa `extractor_maestro.py` para uso programático
    """)

# ============================================
# FOOTER - OCULTO
# ============================================

# st.markdown("<div style='margin-top: 4rem;'></div>", unsafe_allow_html=True)

# st.markdown("""
# <div style="background: linear-gradient(135deg, rgba(0, 242, 234, 0.1) 0%, rgba(255, 0, 255, 0.1) 100%); 
#             border-radius: 25px; padding: 3rem 2rem; margin-top: 4rem;
#             box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8),
#                         0 0 40px rgba(0, 242, 234, 0.2);
#             border: 2px solid rgba(0, 242, 234, 0.3);
#             text-align: center;
#             backdrop-filter: blur(20px);">
#     <div style="display: flex; justify-content: center; align-items: center; gap: 1.5rem; margin-bottom: 1.5rem;">
#         <div style="font-size: 3rem; filter: drop-shadow(0 0 10px rgba(0, 242, 234, 0.6));">⚡</div>
#         <h2 style="background: linear-gradient(135deg, #00f2ea 0%, #ff00ff 100%);
#                    -webkit-background-clip: text;
#                    -webkit-text-fill-color: transparent;
#                    font-family: 'Orbitron', sans-serif; 
#                    margin: 0; 
#                    font-weight: 900; 
#                    font-size: 2.5rem;
#                    text-shadow: 0 0 30px rgba(0, 242, 234, 0.5);">
#             DOCUX AI
#         </h2>
#         <div style="font-size: 3rem; filter: drop-shadow(0 0 10px rgba(255, 0, 255, 0.6));">⚡</div>
#     </div>
#     
#     <div style="color: #00f2ea; 
#                 font-size: 1.1rem; 
#                 margin-bottom: 2rem; 
#                 line-height: 1.8;
#                 font-family: 'Rajdhani', sans-serif;
#                 font-weight: 600;
#                 text-transform: uppercase;
#                 letter-spacing: 2px;
#                 text-shadow: 0 0 15px rgba(0, 242, 234, 0.4);">
#         🚀 Sistema de IA de Última Generación en Extracción Documental 🚀
#     </div>
#     
#     <div style="display: flex; justify-content: center; gap: 2.5rem; flex-wrap: wrap; margin-bottom: 2rem;">
#         <div style="color: #00f2ea; font-size: 1rem; font-family: 'Rajdhani', sans-serif; font-weight: 700;">
#             ⚡ <span style="color: #ff00ff;">4</span> Motores OCR
#         </div>
#         <div style="color: #00f2ea; font-size: 1rem; font-family: 'Rajdhani', sans-serif; font-weight: 700;">
#             🧠 <span style="color: #ff00ff;">6</span> Estrategias IA
#         </div>
#         <div style="color: #00f2ea; font-size: 1rem; font-family: 'Rajdhani', sans-serif; font-weight: 700;">
#             ☁️ <span style="color: #ff00ff;">Azure</span> Cloud
#         </div>
#         <div style="color: #00f2ea; font-size: 1rem; font-family: 'Rajdhani', sans-serif; font-weight: 700;">
#             🎯 <span style="color: #ff00ff;">Auto</span>-Learning
#         </div>
#     </div>
#     
#     <div style="border-top: 1px solid rgba(0, 242, 234, 0.3); 
#                 padding-top: 1.5rem; 
#                 margin-top: 1.5rem;">
#         <div style="color: rgba(0, 242, 234, 0.8); 
#                     font-size: 0.9rem;
#                     font-family: 'Rajdhani', sans-serif;
#                     font-weight: 500;">
#             Desarrollado con ⚡ usando Streamlit • OpenCV • PaddleOCR • EasyOCR • Tesseract • Azure AI
#         </div>
#         <div style="color: rgba(0, 242, 234, 0.6); 
#                     font-size: 0.8rem; 
#                     margin-top: 0.8rem;
#                     font-family: 'Rajdhani', sans-serif;">
#             v3.0 PREMIUM | © 2026 | Enterprise Grade AI Solution
#         </div>
#     </div>
# </div>
# """, unsafe_allow_html=True)
