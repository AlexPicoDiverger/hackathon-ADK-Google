# Ejemplo de ADK: Streaming Personalizado con WebSockets

Este proyecto es una implementación autocontenida de un agente conversacional en tiempo real usando el **Agent Development Kit (ADK) de Google**, **FastAPI** y **WebSockets**.

Es el punto de partida ideal para el reto **"Agente por Interlocución de Voz"** del hackathon.

### ¿Cómo Funciona?

-   **Backend (`main.py`):** Un servidor escrito en Python con FastAPI. Crea un agente con el ADK de Google y lo expone a través de un endpoint de WebSocket. El agente puede usar "Tools" (como `get_weather`) para realizar acciones.
-   **Frontend (`index.html`):** Una simple página web que se conecta al servidor WebSocket. Envía los mensajes del usuario y muestra las respuestas del agente token por token, creando un efecto de streaming en tiempo real.

---

### 🚀 Guía de Ejecución Rápida

Sigue estos pasos para ponerlo en marcha en menos de 5 minutos.

https://google.github.io/adk-docs/streaming/custom-streaming-ws/

-   Abre tu navegador web (Chrome, Firefox, etc.).
-   Ve a la dirección: **`http://localhost:8000`**

¡Listo! Ahora puedes interactuar con tu agente. Prueba a preguntarle: *"¿Qué tiempo hace en Madrid?"*.

---

### 💡 Ideas para Extender el Proyecto

-   **Añade nuevas Tools:** Crea funciones Python con el decorador `@tool` para conectar tu agente a APIs externas (noticias, deportes, tu propia API...).
-   **Cambia la personalidad:** Modifica la `system_instruction` en `main.py` para que el agente se comporte de forma diferente.
-   **Mejora la interfaz:** Modifica el `index.html` para darle un nuevo look.
-   **Añade memoria:** Utiliza el [framework de memoria del ADK](https://google.github.io/adk-docs/guides/memory/) para que el agente recuerde información entre conversaciones.