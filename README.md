<div align="center">

# 🦄 Pegasus Agente Empresarial

### Sistema de Inteligencia Artificial basado en RAG para consulta inteligente de documentación empresarial

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-RAG-success)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-orange)
![Groq](https://img.shields.io/badge/Groq-LLM-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

Sistema desarrollado para responder preguntas sobre documentación empresarial utilizando **Inteligencia Artificial**, **RAG (Retrieval-Augmented Generation)** y **Modelos de Lenguaje de Gran Escala (LLM)**.

</div>

---

# 🎥 Demostración

Conoce Pegasus Agente Empresarial en funcionamiento.

[![Ver demostración](https://img.youtube.com/vi/cnaN0yqoGPI/maxresdefault.jpg)](https://youtu.be/cnaN0yqoGPI)

▶ **Video completo**

https://youtu.be/cnaN0yqoGPI

---

# 📖 Descripción

Pegasus Agente Empresarial es un asistente inteligente diseñado para consultar documentos empresariales mediante lenguaje natural.

El sistema emplea una arquitectura **RAG (Retrieval-Augmented Generation)** que combina recuperación semántica de información con modelos de lenguaje para entregar respuestas precisas, contextualizadas y fáciles de comprender.

Actualmente permite consultar documentos PDF indexados en una base vectorial utilizando una interfaz web desarrollada con FastAPI.

---

# 🚀 ¿Por qué Pegasus?

En muchas organizaciones la información está distribuida entre cientos de documentos PDF, manuales, políticas y procedimientos.

Pegasus reduce el tiempo de búsqueda permitiendo que cualquier usuario realice preguntas en lenguaje natural y obtenga respuestas fundamentadas en la documentación disponible.

Esto facilita:

- Acceso rápido al conocimiento corporativo.
- Reducción del tiempo de búsqueda.
- Mejor aprovechamiento de la documentación empresarial.
- Mayor productividad de los colaboradores.

---

# ✨ Características

- Consulta inteligente de documentos PDF.
- Arquitectura basada en RAG.
- Búsqueda semántica mediante ChromaDB.
- Integración con modelos LLM utilizando Groq.
- Interfaz Web moderna.
- API REST desarrollada con FastAPI.
- Arquitectura modular y escalable.
- Preparado para futuras integraciones.

---

# 🏗 Arquitectura

```
                   Usuario
                      │
                      ▼
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
          ┌───────────┴───────────┐
          ▼                       ▼
    Retriever               Prompt Builder
          │
          ▼
       ChromaDB
          │
          ▼
        Groq LLM
          │
          ▼
      Respuesta Final
```

---

# ⚙ Tecnologías

- Python 3.11
- FastAPI
- LangChain
- ChromaDB
- Groq API
- Sentence Transformers
- PyMuPDF
- Uvicorn
- HTML5
- CSS3
- JavaScript

---

# 📦 Dependencias

Las dependencias completas del proyecto se encuentran en:

```
requirements.txt
```

Instalación:

```bash
pip install -r requirements.txt
```

---

# 📁 Estructura del Proyecto

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
├── agente.py
├── chunking.py
├── lector_documentos.py
├── lector_pdf.py
│├── config/
├── core/
├── llm/
├── memory/
├── models/
├── rag/
└── services/

documentos/
vector_db/

main.py
requirements.txt
README.md
```

---

# 🚀 Instalación

Clonar el repositorio.

```bash
git clone https://github.com/FredyPachon/pegasus-knowledge-ai.git
```

Entrar al proyecto.

```bash
cd pegasus-knowledge-ai
```

Activar el entorno virtual.

```bash
conda activate pegasus-v2
```

Instalar dependencias.

```bash
pip install -r requirements.txt
```

---

# ▶ Ejecución

Iniciar el servidor.

```bash
uvicorn frontend.server:app --reload
```

Abrir el navegador.

```
http://127.0.0.1:8000
```

---

# 💬 Ejemplo de uso

Pregunta:

```
¿Qué es el Back-End?
```

Respuesta:

```
Pegasus buscará la información en la base documental y generará una respuesta utilizando el modelo LLM conectado mediante Groq.
```

---

# 🛣 Roadmap

## Versión 1.0

- Motor RAG funcional.
- ChromaDB.
- FastAPI.
- Interfaz Web.
- Integración con Groq.
- Consulta inteligente de documentos.

---

## Próximas versiones futuras para ser aplicadas en otros Modelos de Agentes

- Historial de conversaciones.
- Memoria conversacional.
- Administración de documentos desde la interfaz.
- Reindexación automática.
- Panel administrativo.
- Gestión de usuarios.
- Control de permisos.
- Integración con múltiples formatos documentales.

---

# 🤝 Contribuciones

Las contribuciones son bienvenidas.

Si deseas colaborar:

1. Haz un Fork.
2. Crea una rama.
3. Realiza tus cambios.
4. Envía un Pull Request.

---

# 📄 Licencia

Este proyecto está distribuido bajo la licencia MIT.

---

# 👨‍💻 Autor

**Fredy Pachon**

Proyecto desarrollado como parte de **Pegasus Agente Empresarial**, una iniciativa enfocada en el desarrollo de soluciones de Inteligencia Artificial para la gestión y consulta inteligente del conocimiento empresarial.

---

# 🙏 Agradecimientos

Este proyecto ha sido posible gracias al ecosistema Open Source y a las herramientas que impulsan el desarrollo moderno de aplicaciones de Inteligencia Artificial, entre ellas Python, FastAPI, LangChain, ChromaDB y Groq.

**Oracle - Alura - LATAM**

Agradecimiento por la documentacion para el proceso de formacion suministrada con altos estanderes academicos en Ingeniería de Agentes, Automatización con IA, Desarrollo y Orquestación con IA Generativa, Inteligencia de Datos y RAG Avanzado ORACLE - ONE AI FOR TECH 2026.

---

<div align="center">

## ⭐ Si este proyecto te resulta útil, considera darle una estrella al repositorio.

**Pegasus Agente Empresarial • Versión 1.0**

</div>