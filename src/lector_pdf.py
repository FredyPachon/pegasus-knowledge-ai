import fitz
from pathlib import Path

from src.models.pagina import PaginaDocumento


def leer_pdf(ruta_pdf: Path):

    documento = fitz.open(ruta_pdf)

    paginas = []

    for numero_pagina, pagina in enumerate(documento, start=1):

        pagina_documento = PaginaDocumento(
            numero=numero_pagina,
            texto=pagina.get_text()
        )

        paginas.append(pagina_documento)

    documento.close()

    return paginas