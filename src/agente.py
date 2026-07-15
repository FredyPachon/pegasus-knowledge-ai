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
    # CHAT
    # ======================================================

    def preguntar(self):

        while True:

            pregunta = input("\n💬 Pregunta (salir): ").strip()

            if pregunta.lower() == "salir":

                print("\n👋 Hasta pronto Ingeniero.\n")
                break

            documentos = self.retriever.buscar(pregunta)

            if not documentos:

                print("\n❌ No encontré información relevante.\n")
                continue

            prompt = self.prompt_builder.construir(
                pregunta,
                documentos
            )

            print("\n🤖 Analizando documentación...\n")

            respuesta = self.llm.generar_respuesta(prompt)

            print("\n" + "=" * 60)
            print("📌 RESPUESTA")
            print("=" * 60)
            print(respuesta)

            print("\n" + "=" * 60)
            print("📚 FUENTES CONSULTADAS")
            print("=" * 60)

            fuentes = set()

            for documento in documentos:

                fuente = (
                    documento.metadata.get("documento"),
                    documento.metadata.get("pagina")
                )

                if fuente not in fuentes:

                    fuentes.add(fuente)

                    print(f"• {fuente[0]} (Página {fuente[1]})")

            print("=" * 60)