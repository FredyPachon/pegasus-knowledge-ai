from src.rag.retriever import PegasusRetriever
from src.rag.reranker import PegasusReranker
from src.rag.prompt_builder import PromptBuilder
from src.llm.groq_provider import GroqProvider


class AgentePegasus:
    """
    Agente principal de Pegasus Knowledge AI.
    """

    def __init__(self):

        self.retriever = PegasusRetriever()

        self.reranker = PegasusReranker(top_n=3)

        self.prompt_builder = PromptBuilder()

        self.llm = GroqProvider()

    # ======================================================
    # INICIO
    # ======================================================

    def iniciar(self):

        print("\n" + "=" * 60)
        print("🚀 PEGASUS KNOWLEDGE AI")
        print("=" * 60)

        print("🧠 LLM          : Groq")
        print("📚 Motor RAG    : LangChain + ChromaDB")
        print("🎯 Re-Ranker    : Pegasus Ranking Engine")

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

            resultados = self.retriever.buscar(pregunta)

            if not resultados:

                print("\n❌ No encontré información.\n")
                continue

            documentos = self.reranker.rerank(resultados)

            prompt = self.prompt_builder.construir(
                pregunta,
                documentos
            )

            print("\n🤖 Analizando documentación...\n")

            respuesta = self.llm.generar_respuesta(prompt)

            print("=" * 60)
            print(respuesta)
            print("=" * 60)

            print("\n📚 Fuentes utilizadas:\n")

            for documento in documentos:

                print(
                    f"• {documento.metadata.get('documento')} "
                    f"(Página {documento.metadata.get('pagina')})"
                )

            print("\n" + "=" * 60)