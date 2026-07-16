from uuid import uuid4

from langchain_core.documents import Document

from src.rag.vector_store import PegasusVectorStore


class PegasusIndexer:
    """
    Constructor de la Base Vectorial de Pegasus.

    Responsabilidades:
    - Convertir fragmentos en Document.
    - Indexarlos en ChromaDB.
    - Evitar duplicados.
    """

    def __init__(self):

        self.vector_store = PegasusVectorStore()
        self.db = self.vector_store.get_db()

    def indexar(self, biblioteca):

        print("\n📚 Construyendo índice vectorial...")

        documentos = []
        ids = []

        for fragmento in biblioteca.fragmentos:

            documento = Document(
                page_content=fragmento.texto,
                metadata={
                    "documento": fragmento.documento,
                    "pagina": fragmento.pagina
                }
            )

            documentos.append(documento)

            # ID único por documento, página y contenido
            ids.append(
                f"{fragmento.documento}_{fragmento.pagina}_{hash(fragmento.texto)}"
            )

        # Elimina IDs repetidos
        unicos = {}
        for doc, doc_id in zip(documentos, ids):
            unicos[doc_id] = doc

        ids = list(unicos.keys())
        documentos = list(unicos.values())

        # Agrega únicamente documentos únicos
        self.db.add_documents(
            documents=documentos,
            ids=ids
        )

        print(f"\n✅ {len(documentos)} fragmentos indexados correctamente.")