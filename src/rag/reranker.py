class PegasusReranker:
    """
    Re-ranker de Pegasus.

    Elimina duplicados y conserva únicamente
    los documentos más relevantes.
    """

    def __init__(self, top_n: int = 3):

        self.top_n = top_n

    def rerank(self, resultados):

        # Menor score = mayor similitud
        resultados = sorted(resultados, key=lambda x: x[1])

        documentos = []
        vistos = set()

        for documento, score in resultados:

            clave = (
                documento.metadata.get("documento"),
                documento.metadata.get("pagina")
            )

            if clave in vistos:
                continue

            vistos.add(clave)

            documentos.append(documento)

            if len(documentos) >= self.top_n:
                break

        return documentos