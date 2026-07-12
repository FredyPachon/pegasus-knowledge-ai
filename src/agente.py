from src.core.biblioteca import BibliotecaConocimiento
from src.services.vector_service import VectorService


class AgentePegasus:
    """
    Agente principal de Pegasus Knowledge AI.

    Coordina el flujo entre el usuario y el motor de búsqueda
    semántica.
    """

    def __init__(
        self,
        biblioteca: BibliotecaConocimiento,
        vector_service: VectorService
    ):

        self.biblioteca = biblioteca
        self.vector_service = vector_service

    # =======================================================
    # INICIO
    # =======================================================

    def iniciar(self):

        print("\n" + "=" * 60)
        print("🚀 PEGASUS KNOWLEDGE AI")
        print("=" * 60)

        print(f"📚 Documentos : {self.biblioteca.total_documentos}")
        print(f"🧩 Fragmentos : {self.biblioteca.total_fragmentos}")
        print(f"🧠 Vectores   : {self.vector_service.total_vectores}")

        print("=" * 60)

    # =======================================================
    # CHAT
    # =======================================================

    def preguntar(self):

        while True:

            consulta = input("\n💬 Pregunta (salir): ").strip()

            if consulta.lower() == "salir":

                print("\n👋 Hasta pronto Ingeniero.\n")
                break

            resultados = self.vector_service.buscar(consulta)

            print("\n")

            if not resultados:

                print("❌ No encontré información.")
                continue

            print("=" * 60)
            print(f"📌 Se encontraron {len(resultados)} fragmentos relevantes.\n")

            for resultado in resultados:

                print(f"📄 Documento : {resultado.documento}")
                print(f"📄 Página    : {resultado.pagina}\n")

                print(resultado.texto)
                print("\n" + "-" * 60)