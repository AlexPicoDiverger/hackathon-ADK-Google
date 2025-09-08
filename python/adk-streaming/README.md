# Ejemplo de ADK: Streaming Personalizado con WebSockets

Este proyecto es una implementación autocontenida de un agente conversacional en tiempo real usando el **Agent Development Kit (ADK) de Google**, **FastAPI** y **WebSockets**.

Es el punto de partida ideal para el reto **"Agente por Interlocución de Voz"** del hackathon.

### ¿Cómo Funciona?

-   **Backend (`main.py`):** Un servidor escrito en Python con FastAPI. Crea un agente con el ADK de Google y lo expone a través de un endpoint de WebSocket. El agente puede usar "Tools" (como `get_weather`) para realizar acciones.
-   **Frontend (`index.html`):** Una simple página web que se conecta al servidor WebSocket. Envía los mensajes del usuario y muestra las respuestas del agente token por token, creando un efecto de streaming en tiempo real.

---

### 🚀 Guía de Ejecución Rápida

Sigue estos pasos para ponerlo en marcha en menos de 5 minutos.

#### 1. Obtén tu Clave de API de Gemini

Necesitarás una clave de API para usar el modelo Gemini de Google.
-   Ve a **[Google AI Studio](https://aistudio.google.com/app/apikey)**.
-   Haz clic en "Create API key" para generar una nueva clave.
-   Cópiala. La necesitarás en el siguiente paso.

#### 2. Configura tu Clave de API

-   Renombra el archivo `.env.example` a `.env`.
-   Abre el nuevo archivo `.env` y pega tu clave de API donde se indica.

    ```
    API_KEY="aquí-va-tu-clave-copiada"
    ```

#### 3. Prepara tu Entorno e Instala Dependencias

Es una buena práctica usar un entorno virtual de Python.

```bash
# 1. Crea un entorno virtual
python -m venv venv

# 2. Actívalo
#    En macOS/Linux:
source venv/bin/activate
#    En Windows:
#    .\venv\Scripts\activate

# 3. Instala todas las librerías necesarias
pip install -r requirements.txt
```

#### 4. Ejecuta el Servidor Backend

Con tu entorno virtual activado, ejecuta el siguiente comando en tu terminal:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
-   `uvicorn` es el servidor que ejecuta nuestra aplicación `FastAPI`.
-   `--reload` hace que el servidor se reinicie automáticamente si haces cambios en el código.

Verás una salida que indica que el servidor está corriendo en `http://0.0.0.0:8000`.

#### 5. Abre el Frontend y ¡Chatea!

-   Abre tu navegador web (Chrome, Firefox, etc.).
-   Ve a la dirección: **`http://localhost:8000`**

¡Listo! Ahora puedes interactuar con tu agente. Prueba a preguntarle: *"¿Qué tiempo hace en Madrid?"*.

---

### 💡 Ideas para Extender el Proyecto

-   **Añade nuevas Tools:** Crea funciones Python con el decorador `@tool` para conectar tu agente a APIs externas (noticias, deportes, tu propia API...).
-   **Cambia la personalidad:** Modifica la `system_instruction` en `main.py` para que el agente se comporte de forma diferente.
-   **Mejora la interfaz:** Modifica el `index.html` para darle un nuevo look.
-   **Añade memoria:** Utiliza el [framework de memoria del ADK](https://google.github.io/adk-docs/guides/memory/) para que el agente recuerde información entre conversaciones.