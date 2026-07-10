from dataclasses import dataclass


@dataclass
class PaginaDocumento:
    """
    Representa una página de un documento.
    """

    numero: int
    texto: str