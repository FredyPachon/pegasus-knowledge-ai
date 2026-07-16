# Pegasus Agente Empresarial

Sistema de Inteligencia Artificial basado en RAG (Retrieval-Augmented Generation) para consultar documentación empresarial mediante lenguaje natural.

Pegasus permite realizar preguntas sobre documentos PDF de una organización y obtener respuestas contextualizadas utilizando búsqueda semántica y un modelo de lenguaje.

---

# Tecnologías

- Python 3.11
- FastAPI
- LangChain
- ChromaDB
- Groq API
- HTML
- CSS
- JavaScript

---

# Arquitectura

```
Usuario
    │
    ▼
Frontend (HTML + CSS + JavaScript)
    │
    ▼
FastAPI
    │
    ▼
Pegasus Service
    │
    ▼
Agente Pegasus
    │
    ▼
Retriever
    │
    ▼
ChromaDB
    │
    ▼
Groq
```

---

# Estructura del proyecto

```
frontend/
│
├── api/
├── services/
├── static/
├── templates/
└── server.py

src/
│
├── rag/
├── llm/
├── core/
├── models/
└── ...

documentos/
vector_db/

main.py
requirements.txt
README.md
```

---

# Instalación

```bash
git clone https://github.com/FredyPachon/pegasus-knowledge-ai.git

cd pegasus-knowledge-ai

conda activate pegasus-v2

pip install -r requirements.txt
```

---

# Ejecutar Pegasus

```bash
uvicorn frontend.server:app --reload
```

Abrir en el navegador:

```
http://127.0.0.1:8000
```

---

# Características

- Consulta inteligente sobre documentos PDF.
- Motor RAG con búsqueda semántica.
- Base vectorial con ChromaDB.
- Respuestas generadas mediante Groq.
- Arquitectura web basada en FastAPI.
- Interfaz desarrollada con HTML, CSS y JavaScript.

---

# Roadmap

### v0.8

- Motor RAG estable.
- Integración con ChromaDB.
- Integración con Groq.
- FastAPI.
- Interfaz Web.
- Consulta desde navegador.

### Próximas versiones

- Mejoras visuales.

---

# Licencia

MIT License.

---

## Autor

**Fredy Pachon**

Proyecto desarrollado como parte de la creación de **Pegasus Agente Empresarial**, una plataforma de IA para consulta inteligente de documentación Corporativa suministrada  gracias el proceso  estudio de alura-Latam Tech - AI - Builder .