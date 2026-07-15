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

        return documentos