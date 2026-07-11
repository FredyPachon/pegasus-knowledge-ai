# 🚀 Pegasus Knowledge AI

> Agente Empresarial Inteligente basado en RAG, Embeddings, LLMs y Búsqueda Semántica.

---

# 📌 Descripción

Pegasus Knowledge AI es un agente inteligente diseñado para responder preguntas sobre la documentación interna de una empresa utilizando Inteligencia Artificial.

El proyecto implementa una arquitectura RAG (Retrieval Augmented Generation) desarrollada completamente en Python y orientada a soluciones empresariales.

Actualmente Pegasus es capaz de:

- Leer documentos PDF.
- Construir una biblioteca de conocimiento.
- Dividir documentos en fragmentos inteligentes.
- Generar embeddings mediante Sentence Transformers.
- Preparar la información para búsqueda semántica.

---

# 🏗 Arquitectura

```
Usuario
    │
    ▼
Pregunta
    │
    ▼
Embedding Service
    │
    ▼
Vector Store
    │
    ▼
Buscador Semántico
    │
    ▼
LLM (OCI)
    │
    ▼
Respuesta
```

---

# 📁 Estructura del proyecto

```
src/
│
├── core/
├── models/
├── services/
├── rag/
├── tests/
│
├── agente.py
└── __init__.py

documentos/
pruebas/
main.py
requirements.txt
```

---

# ⚙ Tecnologías

- Python
- PyMuPDF
- Sentence Transformers
- NumPy
- Git
- GitHub

Próximamente:

- FAISS
- OCI Generative AI
- WhatsApp Business API

---

# 🚀 Estado del proyecto

Versión actual:

**v0.2**

Estado:

🟢 En desarrollo.

---

# 🛣 Roadmap

## ✅ Fase I

- Arquitectura
- Base documental
- Git
- GitHub

---

## 🚧 Fase II

- Embeddings
- Vector Store
- Búsqueda Semántica

---

## ⏳ Fase III

- Integración LLM OCI
- Pipeline RAG
- Generación de respuestas

---

## ⏳ Fase IV

- Memoria conversacional
- Historial
- Contexto

---

## ⏳ Fase V

- API REST
- WhatsApp
- Panel Web
- Multiempresa

---

# 🎯 Objetivo

Construir un asistente empresarial capaz de comprender documentos internos y responder preguntas utilizando Inteligencia Artificial.

---

# 👨‍💻 Autor

**Fredy Pachón**

Proyecto desarrollado como parte del proceso de formación en Ingeniería de Inteligencia Artificial y construcción de agentes empresariales.

---

# 📜 Licencia

MIT License