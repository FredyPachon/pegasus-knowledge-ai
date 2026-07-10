from dataclasses import dataclass, field


@dataclass
class DocumentoEmpresa:
    """
    Representa un documento oficial perteneciente
    a la base de conocimiento de Pegasus.
    """

    nombre: str
    ruta: str
    paginas: list = field(default_factory=list)

    # ==========================================================
    # PROPIEDADES
    # ==========================================================

    @property
    def total_paginas(self):

        return len(self.paginas)

    @property
    def total_caracteres(self):

        return sum(len(pagina.texto) for pagina in self.paginas)

    # ==========================================================
    # REPRESENTACIÓN
    # ==========================================================

    def __repr__(self):

        return (
            f"DocumentoEmpresa("
            f"nombre='{self.nombre}', "
            f"paginas={self.total_paginas}, "
            f"caracteres={self.total_caracteres})"
        )