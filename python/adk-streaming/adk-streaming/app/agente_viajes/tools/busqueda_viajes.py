# Simplified travel search tools for ADK - returns demo data for searches
from typing import Any, Dict, List
from google.adk.tools import FunctionTool

def tool_buscar_vuelos(
    origen: str = "MAD",
    destino: str = "AMS", 
    fecha_salida: str = "15/01/2025",
    fecha_regreso: str = "22/01/2025",
    pasajeros: int = 1
) -> Dict[str, Any]:
    """Busca vuelos entre dos ciudades (demo data)."""
    return {
        "status": "success",
        "vuelos_encontrados": [
            {
                "origen": origen,
                "destino": destino,
                "fecha_salida": fecha_salida,
                "fecha_regreso": fecha_regreso,
                "pasajeros": pasajeros,
                "precio": "450 EUR",
                "aerolinea": "Iberia",
                "duracion": "2h 30m",
                "escalas": 0,
                "clase": "Económica",
                "numero_vuelo": "IB1234"
            },
            {
                "origen": origen,
                "destino": destino,
                "fecha_salida": fecha_salida,
                "fecha_regreso": fecha_regreso,
                "pasajeros": pasajeros,
                "precio": "380 EUR",
                "aerolinea": "Vueling",
                "duracion": "2h 45m",
                "escalas": 0,
                "clase": "Económica",
                "numero_vuelo": "VY5678"
            },
            {
                "origen": origen,
                "destino": destino,
                "fecha_salida": fecha_salida,
                "fecha_regreso": fecha_regreso,
                "pasajeros": pasajeros,
                "precio": "520 EUR",
                "aerolinea": "Air Europa",
                "duracion": "2h 15m",
                "escalas": 0,
                "clase": "Económica",
                "numero_vuelo": "UX9012"
            }
        ],
        "mensaje": f"✅ Encontrados 3 vuelos de {origen} a {destino} para {pasajeros} pasajero(s)"
    }

def tool_crear_itinerario(
    destino: str = "Tokio",
    dias: int = 7,
    presupuesto: int = 1200
) -> Dict[str, Any]:
    """Crea un itinerario de viaje personalizado (demo data)."""
    return {
        "status": "success",
        "itinerario": {
            "destino": destino,
            "duracion": f"{dias} días",
            "presupuesto_estimado": f"{presupuesto} EUR",
            "actividades": [
                "Día 1: Llegada y exploración del centro",
                "Día 2: Visita al templo Senso-ji",
                "Día 3: Excursión a Nikko",
                "Día 4: Mercado de Tsukiji y Ginza",
                "Día 5: Palacio Imperial y jardines",
                "Día 6: Harajuku y Shibuya",
                "Día 7: Regreso"
            ],
            "hoteles_sugeridos": [
                "Hotel Park Hyatt Tokyo - 5 estrellas",
                "Hotel Gracery Shinjuku - 4 estrellas",
                "Capsule Hotel - Económico"
            ],
            "restaurantes": [
                "Sushi Dai (Tsukiji)",
                "Ramen Ichiran",
                "Tempura Kondo"
            ],
            "transporte": [
                "JR Pass para transporte local",
                "Taxi desde el aeropuerto",
                "Metro para moverse por la ciudad"
            ]
        },
        "mensaje": f"✅ Itinerario de {dias} días para {destino} creado con presupuesto de {presupuesto} EUR"
    }

# Create FunctionTool instances
tool_vuelos = FunctionTool(tool_buscar_vuelos)
tool_itinerario = FunctionTool(tool_crear_itinerario)
