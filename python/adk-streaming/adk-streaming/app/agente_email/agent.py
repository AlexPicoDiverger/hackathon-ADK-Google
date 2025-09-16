# Copyright 2025 Alejandro Pico
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Agente Email: Gestión de emails con sub-agente para redacción contextual."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from agente_email.sub_agentes.redactor_emails import redactor_emails_agent
from agente_email.tools.envio_email import herramienta_envio_email

MODEL = "gemini-2.0-flash-exp"
# Agente Email Principal
agente_email = LlmAgent(
    name="agente_email",
    model=MODEL,
    description=(
        "Agente especializado en la gestión y envío de emails. "
        "Coordina la redacción contextual de emails y su envío, "
        "proporcionando un servicio completo de comunicación por correo electrónico."
    ),
    instruction="""
Eres un asistente especializado en gestión de emails. Tu función es:

1. COORDINACIÓN DE EMAILS:
   - Analizar solicitudes de envío de emails
   - Determinar el contexto y tono apropiado
   - Delegar la redacción al sub-agente especializado
   - Coordinar el envío del email

2. GESTIÓN DE COMUNICACIONES:
   - Procesar solicitudes de emails formales e informales
   - Manejar notificaciones y confirmaciones
   - Gestionar respuestas automáticas
   - Organizar seguimientos de comunicación

3. COORDINACIÓN CON SUB-AGENTES:
   - Delegar redacción al redactor_emails_agent
   - Proporcionar contexto específico para cada email
   - Revisar y aprobar contenido antes del envío
   - Asegurar coherencia en la comunicación

4. ENVÍO Y SEGUIMIENTO:
   - Enviar emails usando las herramientas disponibles
   - Confirmar entregas y lecturas
   - Programar envíos futuros si es necesario
   - Mantener registro de comunicaciones

IMPORTANTE: Después de completar cualquier tarea de email, SIEMPRE regresa el control al agente orquestador principal. No continúes con conversaciones adicionales - simplemente ejecuta la herramienta solicitada y devuelve el resultado.

Siempre confirma los detalles del email antes de enviarlo.
Proporciona confirmaciones claras de las acciones realizadas.
""",
    output_key="resultado_email",
    tools=[
        AgentTool(agent=redactor_emails_agent),
        herramienta_envio_email,
    ],
)
