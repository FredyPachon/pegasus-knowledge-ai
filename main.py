from src.lector_documentos import construir_biblioteca
from src.agente import AgentePegasus

from src.services.embedding_service import EmbeddingService
from src.services.vector_service import VectorService


def main():

    print("\n🚀 Iniciando Pegasus...\n")

    # ======================================================
    # Construcción de la biblioteca
    # ======================================================

    biblioteca = construir_biblioteca()

    # ======================================================
    # Servicio de Embeddings
    # ======================================================

    embedding_service = EmbeddingService()

    # ======================================================
    # Construcción de la memoria vectorial
    # ======================================================

    vector_service = VectorService(embedding_service)

    vector_service.construir(biblioteca)

    # ======================================================
    # Agente
    # ======================================================

    agente = AgentePegasus(
        biblioteca=biblioteca,
        vector_service=vector_service
    )

    agente.iniciar()

    agente.preguntar()


if __name__ == "__main__":
    main()