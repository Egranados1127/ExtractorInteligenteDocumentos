import pandas as pd
from azure.ai.formrecognizer import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential

# --- CONFIGURACIÓN DESDE ARCHIVO EXTERNO ---
try:
    from config import AZURE_ENDPOINT as endpoint, AZURE_KEY as key, RUTA_IMAGEN as ruta_imagen
    print("✅ Credenciales cargadas desde config.py")
except ImportError:
    print("⚠️  No se encontró config.py. Usando valores por defecto.")
    print("   Crea el archivo config.py con tus credenciales de Azure.")
    endpoint = "PEGA_AQUI_TU_ENDPOINT"
    key = "PEGA_AQUI_TU_KEY_1"
    ruta_imagen = "WhatsApp Image 2026-01-08 at 8.09.55 PM.jpg"

# 1. Conectarse con Azure
client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# 2. Enviar la imagen para que la IA la analice
print("Analizando documento... por favor espera.")
with open(ruta_imagen, "rb") as f:
    poller = client.begin_analyze_document(
        "prebuilt-layout", analyze_request=f, content_type="application/octet-stream"
    )
result = poller.result()

# 3. Extraer la tabla y convertirla a un archivo de Excel
for table in result.tables:
    # Creamos una lista vacía para las filas
    rows = []
    for row_idx in range(table.row_count):
        row = []
        for col_idx in range(table.column_count):
            # Buscamos el contenido de cada celda
            cell_text = ""
            for cell in table.cells:
                if cell.row_index == row_idx and cell.column_index == col_idx:
                    cell_text = cell.content
                    break
            row.append(cell_text)
        rows.append(row)

    # Creamos el Excel con Pandas
    df = pd.DataFrame(rows[1:], columns=rows[0])
    df.to_excel("Cartera_Extraida.xlsx", index=False)
    print("¡Listo! Se ha creado el archivo 'Cartera_Extraida.xlsx'.")
