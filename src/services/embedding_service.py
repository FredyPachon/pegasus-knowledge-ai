from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Servicio encargado de convertir texto en embeddings.
    """

    def __init__(self):

        print("🧠 Cargando modelo de Embeddings...")

        self.modelo = SentenceTransformer("all-MiniLM-L6-v2")

        print("✅ Modelo cargado correctamente.")

    def generar_embedding(self, texto: str):

        return self.modelo.encode(texto)

    def generar_embeddings(self, textos: list[str]):

        return self.modelo.encode(textos)