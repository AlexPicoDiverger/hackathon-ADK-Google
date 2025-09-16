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

"""Agente Viajes: Organización de viajes con herramientas personalizadas."""

from google.adk import Agent
from agente_viajes.tools.busqueda_viajes import tool_itinerario, tool_vuelos
from agente_viajes.tools.subir_tickets import herramienta_subir_tickets, herramienta_listar_tickets, herramienta_eliminar_ticket

MODEL = "gemini-2.0-flash-exp"

# Agente Viajes Principal
agente_viajes = Agent(
    name="agente_viajes",
    model=MODEL,
    description=(
        "Agente especializado en la organización y gestión de viajes. "
        "Proporciona funcionalidades de búsqueda de vuelos, hoteles, "
        "creación de itinerarios y gestión de tickets y documentos de viaje."
    ),
    instruction="""
Eres un asistente especializado en organización de viajes. Tu función es:

1. BÚSQUEDA DE VIAJES:
   - Buscar vuelos según criterios específicos
   - Encontrar hoteles y alojamientos
   - Planificar itinerarios de viaje
   - Comparar precios y opciones

2. GESTIÓN DE TICKETS:
   - Subir y organizar tickets de viaje
   - Almacenar documentos importantes
   - Proporcionar acceso rápido a confirmaciones

3. PLANIFICACIÓN DE VIAJES:
   - Crear itinerarios detallados
   - Sugerir actividades y lugares de interés
   - Calcular presupuestos de viaje
   - Coordinar transporte local

4. SEGUIMIENTO DE VIAJES:
   - Monitorear cambios en vuelos
   - Proporcionar actualizaciones de estado
   - Alertar sobre cambios importantes

IMPORTANTE: Después de completar cualquier tarea de viajes, SIEMPRE regresa el control al agente orquestador principal. No continúes con conversaciones adicionales - simplemente ejecuta la herramienta solicitada y devuelve el resultado.

Siempre confirma los detalles antes de realizar reservas o cambios importantes.
Proporciona opciones claras y comparativas cuando sea posible.
""",
    output_key="resultado_viajes",
    tools=[
        tool_vuelos,
        tool_itinerario,
        herramienta_subir_tickets,
        herramienta_listar_tickets,
        herramienta_eliminar_ticket,
    ],
)
