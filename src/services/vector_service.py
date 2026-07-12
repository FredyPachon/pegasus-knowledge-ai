import numpy as np

from src.services.embedding_service import EmbeddingService


class VectorService:
    """
    Administra la memoria vectorial de Pegasus.

    Responsabilidades:
    - Generar embeddings.
    - Almacenar vectores.
    - Buscar similitud semántica.
    """

    def __init__(self, embedding_service: EmbeddingService):

        self.embedding_service = embedding_service
        self.vectores = []

    # =====================================================
    # CONSTRUCCIÓN
    # =====================================================

    def construir(self, biblioteca):

        print("\n🧠 Construyendo memoria vectorial...\n")

        self.vectores.clear()

        total = len(biblioteca.fragmentos)

        for indice, fragmento in enumerate(biblioteca.fragmentos, start=1):

            embedding = self.embedding_service.generar_embedding(
                fragmento.texto
            )

            self.vectores.append(
                {
                    "embedding": embedding,
                    "fragmento": fragmento,
                }
            )

            if indice % 25 == 0 or indice == total:

                print(f"   {indice}/{total} embeddings creados")

        print(f"\n✅ Memoria vectorial creada ({len(self.vectores)} vectores)\n")

    # =====================================================
    # BÚSQUEDA
    # =====================================================

    def buscar(self, consulta: str, top_k: int = 5):

        embedding_consulta = self.embedding_service.generar_embedding(
            consulta
        )

        resultados = []

        for item in self.vectores:

            similitud = np.dot(
                embedding_consulta,
                item["embedding"],
            ) / (
                np.linalg.norm(embedding_consulta)
                * np.linalg.norm(item["embedding"])
            )

            resultados.append(
                (
                    similitud,
                    item["fragmento"],
                )
            )

        resultados.sort(
            key=lambda x: x[0],
            reverse=True,
        )

        return [
            fragmento
            for _, fragmento in resultados[:top_k]
        ]

    # =====================================================
    # INFORMACIÓN
    # =====================================================

    @property
    def total_vectores(self):

        return len(self.vectores)