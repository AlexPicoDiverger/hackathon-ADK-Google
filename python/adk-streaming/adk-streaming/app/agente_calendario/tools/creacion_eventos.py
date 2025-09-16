# Simplified calendar event creation tools for ADK
from typing import Any, Dict, List
from google.adk.tools import FunctionTool

def placeholder_creacion_eventos() -> Dict[str, Any]:
    """Crea un evento en el calendario (placeholder)."""
    return {
        "status": "success",
        "evento_creado": {
            "titulo": "Reunión de ejemplo",
            "descripcion": "Reunión de demostración creada por el asistente",
            "fecha_inicio": "2024-01-15",
            "hora_inicio": "14:00",
            "fecha_fin": "2024-01-15",
            "hora_fin": "15:00",
            "ubicacion": "Oficina principal",
            "participantes": ["usuario@ejemplo.com"],
            "recordatorio_minutos": 15,
            "calendario_id": "primary",
            "evento_id": "evento_demo_123456",
            "enlace_reunión": "https://meet.google.com/demo-link"
        },
        "mensaje": "✅ Evento establecido con éxito en tu calendario."
    }

def modificar_evento_calendario(
    evento_id: str,
    titulo: str = None,
    descripcion: str = None,
    fecha_inicio: str = None,
    hora_inicio: str = None,
    fecha_fin: str = None,
    hora_fin: str = None,
    ubicacion: str = None,
    calendario_id: str = "primary"
) -> Dict[str, Any]:
    """Modifica un evento existente en el calendario (placeholder)."""
    return {
        "status": "success",
        "evento_modificado": {
            "evento_id": evento_id,
            "titulo": titulo or "Evento modificado",
            "descripcion": descripcion or "Evento actualizado por el asistente",
            "fecha_inicio": fecha_inicio or "2024-01-15",
            "hora_inicio": hora_inicio or "14:00",
            "fecha_fin": fecha_fin or "2024-01-15",
            "hora_fin": hora_fin or "15:00",
            "ubicacion": ubicacion or "Oficina principal",
            "calendario_id": calendario_id
        },
        "mensaje": "✅ Evento modificado exitosamente en tu calendario."
    }

def eliminar_evento_calendario(evento_id: str, calendario_id: str = "primary") -> Dict[str, Any]:
    """Elimina un evento del calendario (placeholder)."""
    return {
        "status": "success",
        "evento_eliminado": {
            "evento_id": evento_id,
            "calendario_id": calendario_id
        },
        "mensaje": "✅ Evento eliminado exitosamente de tu calendario."
    }

# Create FunctionTool instances
herramienta_creacion_eventos = FunctionTool(placeholder_creacion_eventos)
herramienta_modificar_evento = FunctionTool(modificar_evento_calendario)
herramienta_eliminar_evento = FunctionTool(eliminar_evento_calendario)