import numpy as np

from src.services.embedding_service import EmbeddingService


class VectorService:
    """
    Administra la memoria vectorial de Pegasus.

    Responsabilidades:
    - Generar embeddings de todos los fragmentos.
    - Almacenar los vectores en memoria.
    - Buscar los fragmentos más similares a una consulta.
    """

    def __init__(self, embedding_service: EmbeddingService):

        self.embedding_service = embedding_service

        self.vectores = []

    # ======================================================
    # CONSTRUCCIÓN DE LA MEMORIA VECTORIAL
    # ======================================================

    def construir(self, biblioteca):

        print("\n🧠 Construyendo memoria vectorial...\n")

        self.vectores.clear()

        textos = [
            fragmento.texto
            for fragmento in biblioteca.fragmentos
        ]

        embeddings = self.embedding_service.generar_embeddings(textos)

        for fragmento, embedding in zip(
            biblioteca.fragmentos,
            embeddings
        ):

            self.vectores.append(
                {
                    "embedding": embedding,
                    "fragmento": fragmento
                }
            )

        print(f"✅ Vectores creados: {len(self.vectores)}")

    # ======================================================
    # BÚSQUEDA SEMÁNTICA
    # ======================================================

    def buscar(self, consulta: str, top_k: int = 5):

        embedding_consulta = self.embedding_service.generar_embedding(
            consulta
        )

        resultados = []

        for item in self.vectores:

            similitud = np.dot(
                embedding_consulta,
                item["embedding"]
            ) / (
                np.linalg.norm(embedding_consulta)
                * np.linalg.norm(item["embedding"])
            )

            resultados.append(
                (
                    similitud,
                    item["fragmento"]
                )
            )

        resultados.sort(
            key=lambda x: x[0],
            reverse=True
        )

        return [
            fragmento
            for _, fragmento in resultados[:top_k]
        ]

    # ======================================================
    # INFORMACIÓN
    # ======================================================

    @property
    def total_vectores(self):

        return len(self.vectores)