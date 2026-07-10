from src.models.fragmento import Fragmento


class BuscadorConocimiento:
    """
    Primer motor de búsqueda de Pegasus.

    Actualmente realiza una búsqueda por coincidencia
    de texto.

    Más adelante será sustituido internamente por
    Embeddings + FAISS sin modificar el resto del sistema.
    """

    def __init__(self, biblioteca):

        self.biblioteca = biblioteca

    def buscar(self, consulta: str, limite: int = 5):

        consulta = consulta.lower().strip()

        resultados = []

        for fragmento in self.biblioteca.fragmentos:

            if consulta in fragmento.texto.lower():

                resultados.append(fragmento)

        print(f"\n🔍 Fragmentos encontrados: {len(resultados)}")

        return resultados[:limite]