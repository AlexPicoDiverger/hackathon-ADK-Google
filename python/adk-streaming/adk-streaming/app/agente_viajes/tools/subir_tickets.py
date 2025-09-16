# Simplified travel ticket upload tools for ADK
from typing import Any, Dict, List
from google.adk.tools import FunctionTool

def listar_tickets() -> List[Dict[str, Any]]:
    """Lista tickets de viaje almacenados (demo data)."""
    return [
        {
            "ticket_id": "TK001",
            "tipo": "Vuelo",
            "origen": "Madrid",
            "destino": "Barcelona",
            "fecha": "2024-01-20",
            "hora": "08:30",
            "aerolinea": "Iberia",
            "numero_vuelo": "IB1234",
            "asiento": "12A",
            "precio": "89 EUR",
            "estado": "Confirmado"
        },
        {
            "ticket_id": "TK002",
            "tipo": "Hotel",
            "nombre": "Hotel Plaza Barcelona",
            "ubicacion": "Barcelona, España",
            "fecha_entrada": "2024-01-20",
            "fecha_salida": "2024-01-22",
            "habitacion": "Suite 205",
            "precio": "120 EUR/noche",
            "estado": "Reservado"
        },
        {
            "ticket_id": "TK003",
            "tipo": "Tren",
            "origen": "Barcelona Sants",
            "destino": "Valencia Nord",
            "fecha": "2024-01-22",
            "hora": "14:15",
            "operador": "Renfe",
            "numero_tren": "AVE 1234",
            "asiento": "Coche 3, Asiento 15",
            "precio": "45 EUR",
            "estado": "Confirmado"
        }
    ]

def subir_ticket(
    tipo: str = "Vuelo",
    archivo: str = "ticket.pdf",
    descripcion: str = "Ticket de viaje"
) -> Dict[str, Any]:
    """Sube un ticket de viaje (placeholder)."""
    return {
        "status": "success",
        "ticket_subido": {
            "ticket_id": f"TK{hash(archivo) % 10000:04d}",
            "tipo": tipo,
            "archivo": archivo,
            "descripcion": descripcion,
            "fecha_subida": "2024-01-15 10:30:00",
            "tamaño": "2.3 MB",
            "formato": "PDF"
        },
        "mensaje": "✅ Ticket subido exitosamente al sistema."
    }

def eliminar_ticket(ticket_id: str) -> Dict[str, Any]:
    """Elimina un ticket de viaje (placeholder)."""
    return {
        "status": "success",
        "ticket_eliminado": {
            "ticket_id": ticket_id
        },
        "mensaje": "✅ Ticket eliminado exitosamente del sistema."
    }

# Create FunctionTool instances
herramienta_subir_tickets = FunctionTool(subir_ticket)
herramienta_listar_tickets = FunctionTool(listar_tickets)
herramienta_eliminar_ticket = FunctionTool(eliminar_ticket)