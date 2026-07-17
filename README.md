# Pegasus Agente Empresarial

Sistema de Inteligencia Artificial basado en **RAG (Retrieval-Augmented Generation)** para consultar documentación empresarial mediante lenguaje natural.

Pegasus Agente Empresarial permite realizar preguntas sobre documentos PDF y obtener respuestas contextualizadas utilizando búsqueda semántica, ChromaDB y modelos de lenguaje de última generación.

---

# 🎥 Demostración

Mira el funcionamiento de Pegasus Agente Empresarial en el siguiente video:

👉 https://youtu.be/4kHYjKkqiv0

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

```
                    Pegasus Agente Empresarial

               Frontend (HTML + CSS + JavaScript)
                            │
                            ▼
                        FastAPI Server
                            │
                            ▼
                     Pegasus Service
                            │
                            ▼
                      Agente Pegasus
                            │
          ┌─────────────────┴─────────────────┐
          ▼                                   ▼
     Retriever                          Prompt Builder
          │                                   │
          └─────────────────┬─────────────────┘
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
│   ├── css/
│   ├── img/
│   └── js/
├── templates/
└── server.py

src/
│
├── chunking.py
├── lector_documentos.py
├── lector_pdf.py
├── agente.py
│
├── config/
├── core/
├── llm/
├── memory/
├── models/
├── rag/
└── services/

documentos/
vector_db/

README.md
requirements.txt
main.py
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

# Ejecutar la aplicación

```bash
uvicorn frontend.server:app --reload
```

Abrir en el navegador:

```
http://127.0.0.1:8000
```

---

# Características

- Consulta inteligente sobre documentación empresarial.
- Motor RAG con búsqueda semántica.
- Base vectorial mediante ChromaDB.
- Integración con Groq.
- Arquitectura modular y escalable.
- Interfaz Web desarrollada con FastAPI.
- Separación entre Frontend, API y Motor IA.

---

# Roadmap

## Versión 0.8

- Motor RAG estable.
- Embeddings.
- ChromaDB.
- FastAPI.
- Interfaz Web.
- Integración con Groq.

## Próximas versiones

- Historial de conversaciones.
- Gestión de documentos desde la interfaz.
- Reindexación automática.
- Panel administrativo.
- Autenticación de usuarios.
- Despliegue en producción.

---

# Licencia

Este proyecto se distribuye bajo la licencia MIT.

---

# Autor

**Fredy Pachon**

Proyecto desarrollado como parte de **Pegasus Agente Empresarial**, una plataforma de Inteligencia Artificial para consulta inteligente de documentación corporativa.

---

## Agradecimientos

**Oracle - Alura - LATAM**

Agradecimiento por la documentacion para el proceso de formacion suministrada en el projecto TECH-IA-BUILDER ORACLE alura latam 2026.