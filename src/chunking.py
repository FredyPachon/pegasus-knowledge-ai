from src.models.fragmento import Fragmento


class ChunkingInteligente:

    def __init__(self, chunk_size=900):

        self.chunk_size = chunk_size

    def dividir(self, documento):

        fragmentos = []

        contador = 1

        for pagina in documento.paginas:

            texto = pagina.texto

            inicio = 0

            while inicio < len(texto):

                fin = inicio + self.chunk_size

                chunk = texto[inicio:fin]

                fragmento = Fragmento(
                    id=contador,
                    documento=documento.nombre,
                    pagina=pagina.numero,
                    texto=chunk,
                    palabras=len(chunk.split()),
                    caracteres=len(chunk)
                )

                fragmentos.append(fragmento)

                contador += 1

                inicio = fin

        return fragmentos