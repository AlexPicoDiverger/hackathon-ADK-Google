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

"""Agente Calendario: Gestión de eventos con integración a Google Calendar."""

from google.adk import Agent
from agente_calendario.tools.lectura_calendario import herramienta_lectura_calendario
from agente_calendario.tools.creacion_eventos import herramienta_creacion_eventos

MODEL = "gemini-2.0-flash-exp"

# Agente Calendario Principal
agente_calendario = Agent(
    name="agente_calendario",
    model=MODEL,
    description=(
        "Agente especializado en la gestión de calendarios y eventos. "
        "Proporciona funcionalidades de lectura, creación y modificación "
        "de eventos con integración completa a Google Calendar."
    ),
    instruction="""
Eres un asistente especializado en gestión de calendarios. Tu función es:

1. LECTURA DE CALENDARIO:
   - Consultar eventos existentes
   - Mostrar horarios disponibles
   - Verificar conflictos de horarios
   - Proporcionar resúmenes de agenda

2. CREACIÓN DE EVENTOS:
   En caso de que se te requiera la creación de un evento muestra un mesaje de Evento establecido con éxito:
   ✅ Evento establecido con éxito en tu calendario.

IMPORTANTE: Después de completar cualquier tarea de calendario, SIEMPRE regresa el control al agente orquestador principal. No continúes con conversaciones adicionales - simplemente ejecuta la herramienta solicitada y devuelve el resultado.

Proporciona confirmaciones claras de las acciones realizadas.
""",
    output_key="resultado_calendario",
    tools=[
        herramienta_lectura_calendario,
        herramienta_creacion_eventos,
    ],
)
