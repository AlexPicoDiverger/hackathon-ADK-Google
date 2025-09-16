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

"""Agente Orquestador: Coordina calendario, viajes y emails con streaming de voz."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from pathlib import Path
import importlib.util

# Import prompt directly
prompt_spec = importlib.util.spec_from_file_location("prompt", Path(__file__).parent / "prompt.py")
prompt_module = importlib.util.module_from_spec(prompt_spec)
prompt_spec.loader.exec_module(prompt_module)
prompt = prompt_module

# Import Google Search agent for testing
from google_search_agent.agent import root_agent as google_search_agent

# Import calendar agent
calendario_spec = importlib.util.spec_from_file_location("calendario", Path(__file__).parent.parent / "agente_calendario" / "agent.py")
calendario_module = importlib.util.module_from_spec(calendario_spec)
calendario_spec.loader.exec_module(calendario_module)
agente_calendario = calendario_module.agente_calendario

# Import viajes agent
viajes_spec = importlib.util.spec_from_file_location("viajes", Path(__file__).parent.parent / "agente_viajes" / "agent.py")
viajes_module = importlib.util.module_from_spec(viajes_spec)
viajes_spec.loader.exec_module(viajes_module)
agente_viajes = viajes_module.agente_viajes

# Import email agent

MODEL = "gemini-2.0-flash-exp"
# Agente Orquestador Principal
agente_orquestador = LlmAgent(
    name="agente_orquestador",
    model=MODEL,
    description=(
        "Asistente inteligente que coordina la gestión de calendario, "
        "organización de viajes y envío de emails. Proporciona una interfaz "
        "unificada para todas las tareas de productividad personal y profesional "
        "con capacidades de streaming de voz en tiempo real."
    ),
    instruction=prompt.ORQUESTADOR_PROMPT + """

IMPORTANTE: Cuando saludes al usuario por primera vez, simplemente di:
"¡Hola! Soy tu asistente personal y estoy aquí para ayudarte con lo que necesites. ¿En qué puedo asistirte hoy?"

No menciones tus capacidades específicas en el saludo inicial. Deja que el usuario descubra lo que puedes hacer a través de la conversación natural.
""",
    output_key="respuesta_orquestador",
    tools=[
        AgentTool(agent=google_search_agent),
        AgentTool(agent=agente_calendario),
        AgentTool(agent=agente_viajes),
    ],
)

root_agent = agente_orquestador
