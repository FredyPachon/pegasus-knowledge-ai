from src.lector_documentos import construir_biblioteca
from src.rag.indexer import PegasusIndexer
from src.agente import AgentePegasus


def main():

    print("\n🚀 Iniciando Pegasus...\n")

    # ======================================================
    # Biblioteca
    # ======================================================

    biblioteca = construir_biblioteca()

    # ======================================================
    # Indexación
    # ======================================================

    indexer = PegasusIndexer()

    indexer.indexar(biblioteca)

    # ======================================================
    # Agente
    # ======================================================

    agente = AgentePegasus()

    agente.iniciar()

    agente.preguntar()


if __name__ == "__main__":
    main()