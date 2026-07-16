from src.lector_documentos import construir_biblioteca
from src.rag.indexer import PegasusIndexer


def main():

    print("\n" + "=" * 60)
    print("🚀 PEGASUS AGENTE EMPRESARIAL")
    print("📚 INDEXANDO DOCUMENTOS")
    print("=" * 60)

    biblioteca = construir_biblioteca()

    indexer = PegasusIndexer()

    indexer.indexar(biblioteca)

    print("\n✅ Base vectorial actualizada correctamente.")


if __name__ == "__main__":
    main()