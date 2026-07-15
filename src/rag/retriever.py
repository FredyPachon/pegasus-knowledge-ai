from src.config.settings import TOP_K
from src.rag.vector_store import PegasusVectorStore


class PegasusRetriever:
    """
    Retriever oficial de Pegasus.
    """

    def __init__(self):

        self.vector_store = PegasusVectorStore()

        self.db = self.vector_store.get_db()

    def buscar(self, pregunta: str):

        resultados = self.db.similarity_search_with_score(
            pregunta,
            k=TOP_K
        )

        return resultados