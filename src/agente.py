from src.rag.retriever import PegasusRetriever


class AgentePegasus:
    """
    Agente principal de Pegasus.
    """

    def __init__(self):

        self.retriever = PegasusRetriever()

    # ======================================================
    # INICIO
    # ======================================================

    def iniciar(self):

        print("\n" + "=" * 60)
        print("🚀 PEGASUS KNOWLEDGE AI")
        print("=" * 60)

        print("✅ Motor RAG Inicializado")
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

                print("\n❌ No encontré información.\n")
                continue

            print("\n" + "=" * 60)

            print(f"📚 {len(documentos)} documentos recuperados.\n")

            for documento in documentos:

                print(documento.metadata)

                print()

                print(documento.page_content)

                print("\n" + "-" * 60)