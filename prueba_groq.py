from src.llm.groq_provider import GroqProvider

groq = GroqProvider()

respuesta = groq.generar_respuesta(
    "Responde únicamente: 'Pegasus conectado correctamente.'"
)

print("\n")
print(respuesta)
print("\n")