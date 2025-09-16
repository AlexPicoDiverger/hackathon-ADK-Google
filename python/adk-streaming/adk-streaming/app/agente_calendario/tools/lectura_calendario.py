# Simplified calendar reading tools for ADK
from typing import Any, Dict, List
from google.adk.tools import FunctionTool

def placeholder_lectura_calendario() -> Dict[str, Any]:
    """Lee eventos del calendario (placeholder)."""
    return {
        "status": "success",
        "eventos_encontrados": [
            {
                "titulo": "Reunión de equipo",
                "fecha": "2024-01-16",
                "hora_inicio": "10:00",
                "hora_fin": "11:00",
                "ubicacion": "Sala de conferencias A",
                "descripcion": "Reunión semanal del equipo de desarrollo"
            },
            {
                "titulo": "Presentación de proyecto",
                "fecha": "2024-01-17",
                "hora_inicio": "14:00",
                "hora_fin": "15:30",
                "ubicacion": "Auditorio principal",
                "descripcion": "Presentación del nuevo proyecto a la dirección"
            },
            {
                "titulo": "Cita médica",
                "fecha": "2024-01-18",
                "hora_inicio": "09:30",
                "hora_fin": "10:30",
                "ubicacion": "Clínica San José",
                "descripcion": "Revisión médica anual"
            }
        ],
        "mensaje": "✅ Calendario leído exitosamente. Se encontraron 3 eventos próximos."
    }

def listar_calendarios() -> List[Dict[str, Any]]:
    """Lista calendarios disponibles (placeholder)."""
    return [
        {
            "id": "primary",
            "nombre": "Calendario Principal",
            "descripcion": "Calendario personal principal",
            "color": "#1a73e8"
        },
        {
            "id": "trabajo",
            "nombre": "Trabajo",
            "descripcion": "Eventos relacionados con el trabajo",
            "color": "#34a853"
        },
        {
            "id": "personal",
            "nombre": "Personal",
            "descripcion": "Eventos personales y familiares",
            "color": "#fbbc04"
        }
    ]

# Create FunctionTool instances
herramienta_lectura_calendario = FunctionTool(placeholder_lectura_calendario)
herramienta_listar_calendarios = FunctionTool(listar_calendarios)