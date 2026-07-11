from src.services.embedding_service import EmbeddingService

servicio = EmbeddingService()

texto = "Pegasus Knowledge AI"

vector = servicio.generar_embedding(texto)

print("\nDimensiones:", len(vector))
print(vector[:10])