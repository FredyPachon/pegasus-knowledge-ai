from src.core.biblioteca import BibliotecaConocimiento
from src.buscador import BuscadorConocimiento


class AgentePegasus:
    """
    Agente principal de Pegasus Knowledge AI.

    Coordina todo el flujo del sistema.
    """

    def __init__(self, biblioteca: BibliotecaConocimiento):

        self.biblioteca = biblioteca

        self.buscador = BuscadorConocimiento(biblioteca)

    # =======================================================
    # INICIO
    # =======================================================

    def iniciar(self):

        print("\n" + "=" * 60)
        print("🚀 PEGASUS KNOWLEDGE AI")
        print("=" * 60)

        print(f"📚 Documentos : {self.biblioteca.total_documentos}")
        print(f"🧩 Fragmentos : {self.biblioteca.total_fragmentos}")

        print("=" * 60)

    # =======================================================
    # PREGUNTAS
    # =======================================================

    def preguntar(self):

        while True:

            consulta = input("\n💬 Pregunta (salir): ")

            if consulta.lower() == "salir":

                print("\nHasta pronto Ingeniero.\n")

                break

            resultados = self.buscador.buscar(consulta)

            print("\n")

            if not resultados:

                print("❌ No encontré información.")

                continue

            print("=" * 60)

            print(f"Se encontraron {len(resultados)} resultados.\n")

            for resultado in resultados:

                print(f"📄 Documento : {resultado.documento}")

                print(f"📄 Página    : {resultado.pagina}")

                print()

                print(resultado.texto[:500])

                print()

                print("-" * 60)