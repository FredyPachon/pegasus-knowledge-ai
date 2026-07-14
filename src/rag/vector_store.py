from langchain_chroma import Chroma

from src.config.settings import (
    VECTOR_DB_DIR,
    CHROMA_COLLECTION,
)

from src.rag.embedding_provider import EmbeddingProvider


class PegasusVectorStore:
    """
    Base de conocimiento vectorial de Pegasus.

    Responsable de:

    - Crear la colección Chroma.
    - Persistir embeddings.
    - Recuperar la colección existente.
    """

    def __init__(self):

        embeddings = EmbeddingProvider().get_embeddings()

        self.db = Chroma(
            collection_name=CHROMA_COLLECTION,
            embedding_function=embeddings,
            persist_directory=str(VECTOR_DB_DIR)
        )

    def get_db(self):

        return self.db