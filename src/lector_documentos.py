from pathlib import Path

from src.lector_pdf import leer_pdf
from src.models.documento import DocumentoEmpresa
from src.chunking import ChunkingInteligente
from src.core.biblioteca import BibliotecaConocimiento

CARPETA_DOCUMENTOS = Path("documentos")


def construir_biblioteca():

    documentos_pdf = list(CARPETA_DOCUMENTOS.glob("*.pdf"))

    biblioteca = BibliotecaConocimiento()

    chunker = ChunkingInteligente()

    print("=" * 60)
    print("PEGASUS KNOWLEDGE AI")
    print("Construcción de la Base de Conocimiento")
    print("=" * 60)

    for pdf in documentos_pdf:

        paginas = leer_pdf(pdf)

        documento = DocumentoEmpresa(
            nombre=pdf.name,
            ruta=str(pdf),
            paginas=paginas
        )

        biblioteca.agregar_documento(documento)

        fragmentos = chunker.dividir(documento)

        biblioteca.agregar_fragmentos(fragmentos)

        print(f"\n📄 {documento.nombre}")
        print(f"   ✔ Páginas      : {documento.total_paginas}")
        print(f"   ✔ Caracteres   : {documento.total_caracteres}")
        print(f"   ✔ Fragmentos   : {len(fragmentos)}")

    print()

    biblioteca.resumen()

    print("\n✅ Base de conocimiento creada correctamente.")

    return biblioteca


if __name__ == "__main__":
    construir_biblioteca()