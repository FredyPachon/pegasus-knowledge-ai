class PromptBuilder:
    """
    Construye el prompt enviado al LLM.
    """

    def construir(self, pregunta: str, documentos: list) -> str:

        contexto = "\n\n".join(
            [
                f"""
Documento: {doc.metadata.get('documento', '')}
Página: {doc.metadata.get('pagina', '')}

{doc.page_content}
"""
                for doc in documentos
            ]
        )

        return f"""
Eres Pegasus Knowledge AI.

Eres el asistente oficial de Santo Pegasus Soluciones.

Tu misión es ayudar a los empleados respondiendo preguntas utilizando la documentación recuperada.

Reglas:

- Utiliza SIEMPRE la documentación proporcionada como fuente principal.
- Explica la respuesta con tus propias palabras.
- Si varios documentos hablan del mismo tema, intégralos en una única respuesta.
- No copies literalmente párrafos completos salvo que sea imprescindible.
- Si la documentación contiene parte de la respuesta, responde con esa información y aclara lo que está documentado.
- Solo responde "No encontré información suficiente en la documentación disponible." cuando el contexto recuperado no tenga relación con la pregunta.

Contexto:

{contexto}

Pregunta:

{pregunta}

Respuesta:
"""