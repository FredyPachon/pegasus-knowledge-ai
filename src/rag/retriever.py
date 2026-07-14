from src.config.settings import TOP_K
from src.rag.vector_store import PegasusVectorStore


class PegasusRetriever:
    """
    Retriever oficial de Pegasus.
    """

    def __init__(self):

        self.vector_store = PegasusVectorStore()

        self.retriever = self.vector_store.get_db().as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": TOP_K
            }
        )

    def buscar(self, pregunta: str):

        return self.retriever.invoke(pregunta)