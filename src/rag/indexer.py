from uuid import uuid4

from langchain_core.documents import Document

from src.rag.vector_store import PegasusVectorStore


class PegasusIndexer:
    """
    Construye la Base de Conocimiento Vectorial de Pegasus.
    """

    def __init__(self):

        self.db = PegasusVectorStore().get_db()

    def indexar(self, biblioteca):

        documentos = []

        ids = []

        for fragmento in biblioteca.fragmentos:

            documentos.append(
                Document(
                    page_content=fragmento.texto,
                    metadata={
                        "documento": fragmento.documento,
                        "pagina": fragmento.pagina
                    }
                )
            )

            ids.append(str(uuid4()))

        self.db.add_documents(
            documents=documentos,
            ids=ids
        )

        print(f"\n✅ {len(documentos)} fragmentos indexados en ChromaDB.")