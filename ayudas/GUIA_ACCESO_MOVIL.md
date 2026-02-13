# 🚀 GUÍA RÁPIDA: ACCESO MÓVIL EN 3 PASOS

## 📱 Opción 1: Red Local (MÁS FÁCIL - 2 MINUTOS)

### **Requisitos:**
- ✅ PC y móvil conectados a la misma red WiFi

### **Pasos:**

#### **1️⃣ Ejecuta la app en tu PC**
```powershell
.\EJECUTAR_APP.ps1
```

#### **2️⃣ Obtén tu IP local**

La app mostrará algo como:
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.105:8501    👈 ESTA ES TU IP
```

**O averigua tu IP manualmente:**

**Windows:**
```powershell
ipconfig
# Busca "IPv4 Address" en tu adaptador WiFi
# Ejemplo: 192.168.1.105
```

**Mac/Linux:**
```bash
ifconfig | grep "inet "
# Busca la IP que empieza con 192.168
```

#### **3️⃣ Abre la app en tu móvil**

1. Abre el navegador de tu móvil (Chrome, Safari, etc.)
2. Escribe la URL completa: `http://TU_IP:8501`
   - Ejemplo: `http://192.168.1.105:8501`
3. **¡Listo!** 🎉

---

## 🌍 Opción 2: Acceso Desde Internet (15 MINUTOS)

### **Con ngrok (Túnel Temporal - Gratis)**

#### **1️⃣ Instala ngrok**
```powershell
# Windows (con winget)
winget install ngrok

# O descarga desde: https://ngrok.com/download
```

#### **2️⃣ Ejecuta la app**
```powershell
.\EJECUTAR_APP.ps1
```

#### **3️⃣ Crea el túnel (en otra terminal)**
```powershell
ngrok http 8501
```

#### **4️⃣ Obtén tu URL pública**
ngrok te dará una URL como:
```
Forwarding    https://a1b2-12-34-56-78.ngrok-free.app -> http://localhost:8501
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                      ESTA ES TU URL PÚBLICA
```

#### **5️⃣ Accede desde cualquier lugar**
- Abre esa URL en cualquier navegador
- Funciona en cualquier dispositivo con internet
- ⚠️ La URL cambia cada vez que reinicias ngrok (versión gratis)

---

## 🌐 Opción 3: Deploy Permanente (30 MINUTOS)

### **Con Streamlit Cloud (100% Gratis y Permanente)**

#### **1️⃣ Sube tu código a GitHub**

```powershell
# Si no has inicializado git:
.\INICIALIZAR_GIT.bat

# Luego:
git add .
git commit -m "App con captura de cámara"
git push origin main
```

#### **2️⃣ Deploy en Streamlit Cloud**

1. Ve a: [share.streamlit.io](https://share.streamlit.io)
2. Conecta tu cuenta GitHub
3. Selecciona tu repositorio
4. Elige el archivo: `app_maestro.py`
5. Haz click en **"Deploy"**

#### **3️⃣ Obtén tu URL permanente**

Streamlit te dará una URL permanente:
```
https://tu-usuario-repo-nombre.streamlit.app
```

**Ventajas:**
- ✅ URL permanente (no cambia)
- ✅ HTTPS seguro
- ✅ Sin necesidad de tener tu PC encendida
- ✅ Acceso desde cualquier lugar del mundo
- ✅ Gratis para siempre

---

## 📸 CÓMO USAR LA CÁMARA

### **En Móvil (Recomendado):**

1. Abre la app en el navegador de tu móvil
2. Selecciona **"📷 Capturar Foto"**
3. El navegador pedirá permiso para acceder a la cámara → Acepta
4. Apunta al documento:
   - ✅ Asegura buena iluminación
   - ✅ Mantén el celular paralelo al documento
   - ✅ Centra el documento en el encuadre
5. Presiona el botón de captura 📸
6. ¡Listo! La app procesará automáticamente

### **En PC con Webcam:**

1. Abre la app en tu navegador
2. Selecciona **"📷 Capturar Foto"**
3. El navegador pedirá permiso → Acepta
4. Coloca el documento frente a la cámara
5. Captura cuando esté enfocado

---

## ⚡ COMPARACIÓN DE OPCIONES

| Característica | Red Local | ngrok | Streamlit Cloud |
|----------------|-----------|-------|-----------------|
| **Velocidad setup** | ⚡ 2 min | ⚡⚡ 15 min | ⚡⚡⚡ 30 min |
| **Costo** | 🆓 Gratis | 🆓 Gratis | 🆓 Gratis |
| **Requisito PC** | 💻 Encendida | 💻 Encendida | ❌ No necesaria |
| **Alcance** | 📡 Solo WiFi local | 🌍 Internet global | 🌍 Internet global |
| **URL permanente** | ❌ No | ❌ No (cambia) | ✅ Sí |
| **HTTPS** | ❌ No | ✅ Sí | ✅ Sí |
| **Ideal para** | Pruebas rápidas | Demos temporales | Producción |

---

## 🔧 SOLUCIÓN DE PROBLEMAS

### **"No puedo acceder desde el móvil"**

✅ **Verifica que estés en la misma red WiFi:**
- PC y móvil deben estar conectados al mismo router
- Desactiva datos móviles en el celular

✅ **Verifica el firewall:**
```powershell
# Permitir Streamlit en el firewall de Windows:
New-NetFirewallRule -DisplayName "Streamlit" -Direction Inbound -Program "python.exe" -Action Allow
```

✅ **Usa la IP correcta:**
- No uses `localhost` desde el móvil
- Usa la IP que empieza con `192.168.X.X`

### **"La cámara no funciona"**

✅ **Revisa permisos:**
- En Chrome móvil: Settings → Site settings → Camera → Permitir
- En Safari iOS: Settings → Safari → Camera → Permitir

✅ **Usa HTTPS:**
- Las cámaras requieren HTTPS o localhost
- Red local funciona (localhost desde el servidor)
- ngrok y Streamlit Cloud usan HTTPS automáticamente

✅ **Actualiza el navegador:**
- Usa Chrome/Safari actualizados
- Evita navegadores antiguos

### **"La app va lenta desde móvil"**

✅ **Red local es más rápida:**
- Usa WiFi en vez de datos móviles
- Acércate al router

✅ **Optimiza imágenes:**
- No captures en resolución máxima innecesariamente
- La app ya optimiza automáticamente

---

## 💡 TIPS PROFESIONALES

### **Para uso diario:**
- 📱 Red local es perfecta para oficina
- ⚡ ngrok para demos con clientes
- 🌐 Streamlit Cloud para usuarios finales

### **Para trabajo en campo:**
- 🚀 Deploy en Streamlit Cloud
- 📶 Funciona con 4G/5G
- 💾 Descarga resultados directo al celular

### **Para máxima seguridad:**
- 🔒 Red local (sin exposición pública)
- 🔐 VPN corporativa + ngrok
- 🛡️ Streamlit Cloud con autenticación

---

## 📞 SOPORTE

¿Problemas configurando el acceso móvil?

1. Revisa esta guía completa
2. Consulta [MOBILE_FEATURES.md](MOBILE_FEATURES.md)
3. Contacta al equipo de desarrollo

---

**✅ CON ESTAS 3 OPCIONES, TIENES TU APP ACCESIBLE DESDE CUALQUIER LUGAR**  
**🚀 ELIGE LA QUE MEJOR SE ADAPTE A TUS NECESIDADES**  
**📱 ¡COMIENZA A PROCESAR DOCUMENTOS DESDE TU MÓVIL HOY MISMO!**
