from langchain_huggingface import HuggingFaceEmbeddings

from src.config.settings import EMBEDDING_MODEL


class EmbeddingProvider:
    """
    Proveedor oficial de embeddings de Pegasus.

    Toda la aplicación obtiene los embeddings desde aquí.
    Esto permite cambiar el modelo en el futuro sin modificar
    el resto del sistema.
    """

    def __init__(self):

        print("\n🧠 Inicializando modelo de Embeddings...")

        self.embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

        print("✅ Embeddings listos.")

    def get_embeddings(self):

        return self.embeddings