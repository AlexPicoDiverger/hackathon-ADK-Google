# Hackathon: Sistemas de Agentes con Google Cloud

¡Bienvenidos al repositorio oficial del **Hackathon de Sistemas de Agentes**, organizado por Diverger y Google Cloud!

Este repositorio contiene los proyectos base, recursos y guías que necesitarás para empezar a construir tu agente inteligente durante el evento. Nuestro objetivo es que aprendas, experimentes y, sobre todo, ¡te diviertas!

---

## 🚀 ¡Manos a la Obra! Guía de Inicio Rápido

Sigue estos pasos para tener tu entorno listo para la acción.

Hemos preparado un Entorno Virtual donde podrás obtener los recursos necesarios para hacer el lab: Podrás encontrarlo el día del hackathon aqui: https://explore.qwiklabs.com/ registrándote con tu cuenta de registro del hackathon. Durante el día del evento os enseñaremos como utilizar este entorno, etc.


### 1. Prerrequisitos

Asegúrate de tener instalado el siguiente software en tu entorno virtual o máquina:
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Python](https://www.python.org/downloads/) (versión 3.9 o superior)
- (Opcional) [JDK](https://www.oracle.com/java/technologies/downloads/) (si prefieres trabajar con Java)
- (Opcional) [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)

- Instala ADK:
https://google.github.io/adk-docs/get-started/installation/


### 2. Clona este Repositorio

Abre tu terminal y clona este repositorio en tu máquina local:
```bash
git clone "https://github.com/DivergerThinking/hackathon-ADK-Google"
cd hackathon-ADK-Google
```

### 3. Elige tu Desafío y Proyecto Base

Tenemos 3 retos temáticos para inspirarte. Hemos preparado proyectos base para que no empieces desde cero.

🧠 **Agente de Deep Research** 
Un sistema que colabora para investigar a fondo cualquier temática, analizando documentos o papers.`python/academic-research` 

🗣️ **Agente por Interlocución de Voz**
Un agente para gestionar reservas, cobros o soporte, que pueda interactuar en tiempo real. 
`python/custom-streaming`

✨ **Reto de Temática Libre** 
¡Tu idea, tus reglas! Usa las herramientas para construir el agente que siempre has imaginado.
Cualquiera de los anteriores


### 4. Configura tu Proyecto Base (Ejemplo con Python)

1.  **Navega a la carpeta del proyecto que elegiste.** Por ejemplo:
    ```bash
    cd python/academic-research
    ```
2.  **Crea un entorno virtual.** Es una buena práctica para aislar las dependencias de tu proyecto.
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```
3.  **Instala las dependencias.**
    ```bash
    pip install -r requirements.txt
    ```
4.  **¡Instala el proyecto!** Revisa el `README.md` específico dentro de la carpeta del proyecto para ver las instrucciones sobre cómo instalarlo y ejecutarlo.

---

## 🔧 Proyectos Base Explicados

### 1. Agente de Investigación Académica (`python/academic-research`)

-   **¿Qué hace?** Este agente utiliza el ADK (Agent Development Kit) de Google para simular un asistente de investigación. Puede tomar un tema, buscar "papers" (documentos) y determinar si son relevantes o interesantes según ciertos criterios.
-   **Ideal para:** El reto **"Agente de Deep Research"**. Puedes extenderlo para que busque en otras fuentes, resuma los hallazgos o genere un informe.
-   **Fuente original:** [Google ADK Samples - Academic Research](https://github.com/google/adk-samples/tree/main/python/agents/academic-research)

### 2. Agente con Streaming (`python/custom-streaming`)

-   **¿Qué hace?** Este es un ejemplo de streaming bidireccional (BI-DI) con el ADK. Permite que el agente reciba y envíe información en tiempo real, en lugar de esperar a que el usuario termine de hablar.
-   **Ideal para:** El reto **"Agente por Interlocución de Voz"**. Es la base perfecta para cualquier aplicación que necesite una conversación fluida y natural, como un asistente de voz, un bot de soporte en vivo o un sistema de reservas interactivo.
-   **Multi-idioma:** ¡Tenemos ejemplos en Python y Java!
    -   **Python:** [ADK Custom Streaming Docs](https://google.github.io/adk-docs/streaming/custom-streaming/)
    -   **Java:** [ADK Streaming Quickstart Java](https://google.github.io/adk-docs/get-started/streaming/quickstart-streaming-java/)

> **Nota para desarrolladores Java y Node.js:** ¡Sois más que bienvenidos! Aunque los ejemplos principales están en Python, el ADK es compatible con Java y Node.js. Anímate a usar la base de `custom-streaming` en Java o a adaptar los conceptos a Node.js. Si tienes dudas, ¡pregunta a los mentores!
Tienes ejemplos de Agentes en Java aqui: https://github.com/google/adk-samples/tree/main/java/agents


---

## 📚 Recursos y Documentación

¿Eres nuevo con ADK y necesitas practicar antes del hackathon? Échale un vistazo a los siguientes recursos:

https://codelabs.developers.google.com/your-first-agent-with-adk?hl=es-419#0
https://codelabs.developers.google.com/devsite/codelabs/build-agents-with-adk-foundation?hl=es-419#0
https://www.cloudskillsboost.google/course_templates/1275


- Hemos preparado un Entorno Virtual donde podrás obtener los recursos necesarios para hacer el lab:
Podrás encontrarlo el día del hackathon aqui:
https://explore.qwiklabs.com/ registrándote con tu cuenta de registro del hackathon. 
Durante el día del evento os enseñaremos como utilizar este entorno, etc.


Durante el hackathon, daremos 3 "píldoras técnicas" sobre conceptos. Aquí tienes la documentación para ir abriendo boca:

1.  **Como funciona BI-DI Agentes en tiempo real:**
    -   Los agentes pueden utilizar ADK para interactuar con video y voz en real-time y con llamadas de baja latencia.
    -   **Documentación:** [ADK BI-DI Agents](https://google.github.io/adk-docs/get-started/streaming/quickstart-streaming/)

2.  **Uso del Framework de Memoria de Google:**
    -   Para que un agente sea útil, debe recordar interacciones pasadas. Veremos cómo gestionar la memoria a corto y largo plazo.
    -   **Documentación:** [Managing Agent Memory](https://google.github.io/adk-docs/guides/memory/)

3.  **Publicar Agentes en GCP o AgentSpaces:**
    -   Lleva tu agente del local a la nube. Te enseñaremos cómo desplegarlo en Google Cloud Platform o en el futuro AgentSpaces.
    -   **Documentación:** [Deploying an Agent](https://google.github.io/adk-docs/guides/deployment/)

---

## 🏆 Presentación y Criterios de Evaluación

-   **Formato:** Cada equipo dispondrá de 5 minutos para un "Elevator Pitch" y una demo de su proyecto.
-   **Jurado:** El jurado evaluará las propuestas basándose en:
    -   **Innovación y Originalidad:** ¿La idea es creativa y resuelve un problema interesante?
    -   **Ejecución Técnica:** ¿El agente funciona? ¿Qué tan complejo y bien implementado está?
    -   **Uso del ADK y Ecosistema Google:** ¿Se aprovechan las herramientas y conceptos vistos (Tools, Memoria, Streaming)?
    -   **Presentación:** Claridad y capacidad de "vender" vuestro proyecto.

---

## 🙋‍♂️ ¿Necesitas Ayuda?

Durante todo el evento, tendrás a tu disposición un equipo de **mentores de Diverger y Google**. No dudes en levantar la mano o buscarnos si tienes dudas, te atascas con el código o simplemente quieres rebotar una idea.

**¡Estamos aquí para aprender y pasar un buen rato!**
