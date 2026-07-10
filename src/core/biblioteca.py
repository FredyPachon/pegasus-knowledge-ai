from dataclasses import dataclass, field

from src.models.documento import DocumentoEmpresa
from src.models.fragmento import Fragmento


@dataclass
class BibliotecaConocimiento:
    """
    Biblioteca central del conocimiento del agente Pegasus.

    Su única responsabilidad es almacenar los documentos y
    los fragmentos que el agente utilizará posteriormente
    para responder preguntas.
    """

    documentos: list[DocumentoEmpresa] = field(default_factory=list)
    fragmentos: list[Fragmento] = field(default_factory=list)

    # ==========================================================
    # DOCUMENTOS
    # ==========================================================

    def agregar_documento(self, documento: DocumentoEmpresa):

        # Evita agregar el mismo documento dos veces.
        if any(doc.nombre == documento.nombre for doc in self.documentos):
            return

        self.documentos.append(documento)

    def obtener_documento(self, nombre: str):

        for documento in self.documentos:

            if documento.nombre == nombre:

                return documento

        return None

    # ==========================================================
    # FRAGMENTOS
    # ==========================================================

    def agregar_fragmentos(self, nuevos_fragmentos: list[Fragmento]):

        self.fragmentos.extend(nuevos_fragmentos)

    # ==========================================================
    # PROPIEDADES
    # ==========================================================

    @property
    def total_documentos(self):

        return len(self.documentos)

    @property
    def total_fragmentos(self):

        return len(self.fragmentos)

    # ==========================================================
    # INFORMACIÓN
    # ==========================================================

    def resumen(self):

        print("\n" + "=" * 60)
        print("BIBLIOTECA DE CONOCIMIENTO")
        print("=" * 60)

        print(f"📚 Documentos : {self.total_documentos}")
        print(f"🧩 Fragmentos : {self.total_fragmentos}")

        print("=" * 60)

    # ==========================================================
    # REPRESENTACIÓN
    # ==========================================================

    def __repr__(self):

        return (
            f"BibliotecaConocimiento("
            f"documentos={self.total_documentos}, "
            f"fragmentos={self.total_fragmentos})"
        )