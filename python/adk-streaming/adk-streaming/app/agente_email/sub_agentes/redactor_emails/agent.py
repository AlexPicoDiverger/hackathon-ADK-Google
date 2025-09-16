# Simplified email composer agent for ADK
from google.adk import Agent
from google.adk.tools import FunctionTool

MODEL = "gemini-2.0-flash-exp"

def redactar_email(
    destinatario: str = "usuario@ejemplo.com",
    asunto: str = "Asunto del email",
    tipo: str = "formal",
    contenido: str = "Contenido del mensaje"
) -> dict:
    """Redacta un email personalizado (placeholder)."""
    return {
        "status": "success",
        "email_redactado": {
            "destinatario": destinatario,
            "asunto": asunto,
            "tipo": tipo,
            "contenido": f"Estimado/a {destinatario},\n\n{contenido}\n\nAtentamente,\nAsistente ADK",
            "formato": "HTML" if tipo == "formal" else "Texto plano",
            "longitud": len(contenido),
            "timestamp": "2024-01-15 10:30:00"
        },
        "mensaje": "✅ Email redactado exitosamente."
    }

# Create tool
herramienta_redactar_email = FunctionTool(redactar_email)

# Email Composer Agent
agente_redactor_emails = Agent(
    name="agente_redactor_emails",
    model=MODEL,
    description="Agente especializado en redactar emails personalizados",
    instruction="""
Eres un asistente especializado en redacción de emails. Tu función es:

1. REDACTAR EMAILS:
   - Crear emails formales e informales
   - Adaptar el tono según el destinatario
   - Estructurar el contenido de manera clara
   - Incluir saludos y despedidas apropiados

2. TIPOS DE EMAIL:
   - Formales: Para trabajo, clientes, autoridades
   - Informales: Para amigos, familia, colegas cercanos
   - Comerciales: Para marketing y ventas
   - Técnicos: Para documentación y soporte

IMPORTANTE: Después de redactar cualquier email, SIEMPRE regresa el control al agente principal de email. No continúes con conversaciones adicionales - simplemente redacta el email solicitado y devuelve el resultado.

Recuerda: Tu objetivo es crear emails que comuniquen efectivamente el mensaje
mientras mantienen el tono y nivel de formalidad apropiados para cada situación específica.
""",
    output_key="email_redactado",
    tools=[herramienta_redactar_email],
)