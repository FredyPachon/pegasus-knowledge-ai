from src.config.settings import TOP_K
from src.rag.vector_store import PegasusVectorStore


class PegasusRetriever:
    """
    Retriever oficial de Pegasus.

    Recupera los documentos más relevantes desde ChromaDB.
    """

    def __init__(self):

        self.vector_store = PegasusVectorStore()
        self.db = self.vector_store.get_db()

    def buscar(self, pregunta: str):

        documentos = self.db.similarity_search(
            query=pregunta,
            k=TOP_K
        )

        # =====================================================
        # DIAGNÓSTICO TEMPORAL
        # =====================================================

        print("\n" + "=" * 60)
        print("📚 DOCUMENTOS RECUPERADOS POR CHROMADB")
        print("=" * 60)

        if not documentos:
            print("⚠️ No se recuperó ningún documento.")
        else:
            for i, doc in enumerate(documentos, start=1):

                print(f"\n[{i}] Documento : {doc.metadata.get('documento')}")
                print(f"    Página    : {doc.metadata.get('pagina')}")
                print("\nFragmento:\n")

                print(doc.page_content[:300])

                print("\n" + "-" * 60)

        return documentos