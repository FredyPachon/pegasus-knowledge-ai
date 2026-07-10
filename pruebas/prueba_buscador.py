from src.lector_documentos import construir_biblioteca
from src.core.biblioteca import BibliotecaConocimiento
from src.buscador import BuscadorConocimiento


print("\nConstruyendo biblioteca...")

documentos = construir_biblioteca()

biblioteca = BibliotecaConocimiento()

for documento in documentos:

    biblioteca.agregar_documento(documento)

print("\nConstruyendo fragmentos...")

from src.chunking import ChunkingInteligente

chunker = ChunkingInteligente()

for documento in documentos:

    fragmentos = chunker.dividir(documento)

    biblioteca.agregar_fragmentos(fragmentos)

print(f"\nFragmentos cargados: {biblioteca.total_fragmentos}")

buscador = BuscadorConocimiento(biblioteca)

consulta = input("\nPregunta: ")

resultados = buscador.buscar(consulta)

print("\nRESULTADOS\n")

for resultado in resultados[:5]:

    print("-" * 60)

    print(resultado.documento)

    print("Página:", resultado.pagina)

    print(resultado.texto[:300])

print("\nFin de búsqueda.")