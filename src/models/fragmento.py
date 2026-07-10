from dataclasses import dataclass


@dataclass
class Fragmento:
    """
    Unidad mínima de conocimiento utilizada por Pegasus.

    Cada fragmento proviene de una página de un documento
    y será utilizado posteriormente por el buscador,
    FAISS y el modelo de lenguaje (OCI).
    """

    id: int
    documento: str
    pagina: int
    texto: str
    palabras: int
    caracteres: int

    # ==========================================================
    # PROPIEDADES
    # ==========================================================

    @property
    def longitud(self):

        return len(self.texto)

    # ==========================================================
    # REPRESENTACIÓN
    # ==========================================================

    def __repr__(self):

        return (
            f"Fragmento("
            f"documento='{self.documento}', "
            f"pagina={self.pagina}, "
            f"palabras={self.palabras})"
        )