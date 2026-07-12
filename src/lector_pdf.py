from pathlib import Path

import pdfplumber

from src.models.pagina import PaginaDocumento


def leer_pdf(ruta_pdf: Path):
    """
    Lee un archivo PDF y devuelve una lista de objetos
    PaginaDocumento.

    Utiliza pdfplumber como motor de extracción de texto.
    """

    paginas = []

    with pdfplumber.open(ruta_pdf) as documento:

        for numero_pagina, pagina in enumerate(documento.pages, start=1):

            texto = pagina.extract_text()

            if texto is None:
                texto = ""

            pagina_documento = PaginaDocumento(
                numero=numero_pagina,
                texto=texto
            )

            paginas.append(pagina_documento)

    return paginas