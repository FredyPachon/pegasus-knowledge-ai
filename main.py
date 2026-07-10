from src.lector_documentos import construir_biblioteca
from src.agente import AgentePegasus


def main():

    print("\n🚀 Iniciando Pegasus Knowledge AI...\n")

    # ======================================================
    # Construcción de la Base de Conocimiento
    # ======================================================

    biblioteca = construir_biblioteca()

    # ======================================================
    # Creación del Agente
    # ======================================================

    agente = AgentePegasus(biblioteca)

    agente.iniciar()

    # ======================================================
    # Comienza la conversación
    # ======================================================

    agente.preguntar()


if __name__ == "__main__":
    main()