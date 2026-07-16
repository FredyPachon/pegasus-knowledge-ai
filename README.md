# Pegasus Agente Empresarial

Sistema de Inteligencia Artificial basado en **RAG (Retrieval-Augmented Generation)** para consultar documentación empresarial mediante lenguaje natural.

Pegasus permite realizar preguntas sobre documentos PDF y obtener respuestas contextualizadas utilizando búsqueda semántica, ChromaDB y Groq.

---

# 🎥 Demostración

Video de funcionamiento de Pegasus Agente Empresarial.

> **Ver demostración:** [pegasus-demo.mp4](demo/pegasus-demo.mp4)

---

# Tecnologías

- Python 3.11
- FastAPI
- LangChain
- ChromaDB
- Groq API
- HTML5
- CSS3
- JavaScript

---

# Arquitectura

```text
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

```text
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
demo/

README.md
requirements.txt
main.py
```

---

# Instalación

```bash
git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git

cd TU-REPOSITORIO

conda activate pegasus-v2

pip install -r requirements.txt
```

---

# Ejecutar Pegasus

```bash
uvicorn frontend.server:app --reload
```

Abrir en el navegador:

```text
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

## v0.8

- Motor RAG estable.
- ChromaDB.
- Groq.
- FastAPI.
- Interfaz Web.
- Consulta desde navegador.

## Próximas versiones

- Historial de conversaciones.
- Gestión de documentos.
- Reindexación desde la interfaz.
- Panel administrativo.
- Despliegue en producción.

---

# Licencia

MIT License.

---

## Autor

**Fredy Pachon**

Proyecto desarrollado como base de **Pegasus Agente Empresarial**, una plataforma de Inteligencia Artificial para consulta inteligente de documentación corporativa agradecimiento por la documentacion para el proceso de formacion suministrada en el projecto TECH-IA-BUILDER ORACLE alura latam 2026.