import codecs

# Leer el archivo
with codecs.open(r"c:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\MIAppExtraccion\app_maestro.py", "r", "utf-8") as f:
    lines = f.readlines()

# Modificar la línea 593 (índice 592)
lines[592] = '        [" Archivo Único", " Capturar Foto", " Carpeta Completa"],\n'

# Modificar las líneas del help (597-599, índices 596-598)
lines[596] = '         Archivo Único: Procesa un solo documento\n'
lines[597] = '         Capturar Foto: Usa la cámara de tu dispositivo (ideal para móviles)\n'
lines[598] = '         Carpeta Completa: Selecciona múltiples archivos de una carpeta\n'

#Guardar el archivo
with codecs.open(r"c:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\MIAppExtraccion\app_maestro.py", "w", "utf-8") as f:
    f.writelines(lines)

print(" Modos de carga actualizados: Archivo Único, Capturar Foto, Carpeta Completa")
