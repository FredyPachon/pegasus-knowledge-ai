from src.rag.retriever import PegasusRetriever
from src.rag.prompt_builder import PromptBuilder
from src.llm.groq_provider import GroqProvider


class AgentePegasus:
    """
    Agente principal de Pegasus Knowledge AI.
    """

    def __init__(self):

        self.retriever = PegasusRetriever()
        self.prompt_builder = PromptBuilder()
        self.llm = GroqProvider()

    # ======================================================
    # INICIO
    # ======================================================

    def iniciar(self):

        print("\n" + "=" * 60)
        print("🚀 PEGASUS KNOWLEDGE AI")
        print("=" * 60)
        print("🧠 LLM        : Groq")
        print("📚 Motor RAG  : LangChain + ChromaDB")
        print("=" * 60)

    # ======================================================
    # NUEVO MÉTODO PARA FASTAPI
    # ======================================================

    def responder(self, pregunta: str) -> str:

        documentos = self.retriever.buscar(pregunta)

        if not documentos:

            return "No encontré información relevante."

        prompt = self.prompt_builder.construir(
            pregunta,
            documentos
        )

        respuesta = self.llm.generar_respuesta(prompt)

        return respuesta

    # ======================================================
    # CHAT EN CONSOLA
    # ======================================================

    def preguntar(self):

        while True:

            pregunta = input("\n💬 Pregunta (salir): ").strip()

            if pregunta.lower() == "salir":

                print("\n👋 Hasta pronto Ingeniero.\n")
                break

            respuesta = self.responder(pregunta)

            print("\n" + "=" * 60)
            print("📌 RESPUESTA")
            print("=" * 60)
            print(respuesta)
            print("=" * 60)