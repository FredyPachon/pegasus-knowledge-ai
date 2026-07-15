import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


class GroqProvider:
    """
    Cliente oficial de Groq para Pegasus.
    """

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "No se encontró la variable GROQ_API_KEY en el archivo .env"
            )

        self.client = Groq(api_key=api_key)

        self.model = os.getenv(
            "MODEL_NAME",
            "llama-3.3-70b-versatile"
        )

    def generar_respuesta(self, prompt: str) -> str:

        respuesta = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
        )

        return respuesta.choices[0].message.content