# Simplified email sending tools for ADK
from typing import Any, Dict, List
from google.adk.tools import FunctionTool

def placeholder_envio_email() -> Dict[str, Any]:
    """Envía un email (placeholder)."""
    return {
        "status": "success",
        "email_enviado": {
            "destinatario": "usuario@ejemplo.com",
            "remitente": "demo@adkassistant.com",
            "asunto": "Mensaje de demostración",
            "contenido": "Este es un email de demostración enviado por el asistente ADK.",
            "destinatarios_cc": [],
            "destinatarios_bcc": [],
            "archivos_adjuntos": [],
            "formato_html": False,
            "message_id": "email_demo_456789",
            "timestamp": "2024-01-15 10:30:00",
            "estado_entrega": "Entregado simulado"
        },
        "mensaje": "✅ Email enviado exitosamente."
    }

def listar_registros_envio() -> List[Dict[str, Any]]:
    """Lista el historial de emails enviados (placeholder)."""
    return [
        {
            "message_id": "email_001",
            "destinatario": "cliente@empresa.com",
            "asunto": "Propuesta de proyecto",
            "fecha_envio": "2024-01-14 09:15:00",
            "estado": "Entregado",
            "tamaño": "2.5 MB"
        },
        {
            "message_id": "email_002", 
            "destinatario": "equipo@trabajo.com",
            "asunto": "Reunión de seguimiento",
            "fecha_envio": "2024-01-13 16:30:00",
            "estado": "Entregado",
            "tamaño": "1.2 MB"
        },
        {
            "message_id": "email_003",
            "destinatario": "proveedor@servicio.com",
            "asunto": "Consulta sobre servicios",
            "fecha_envio": "2024-01-12 11:45:00",
            "estado": "Entregado",
            "tamaño": "856 KB"
        }
    ]

# Create FunctionTool instances
herramienta_envio_email = FunctionTool(placeholder_envio_email)
herramienta_listar_envios = FunctionTool(listar_registros_envio)