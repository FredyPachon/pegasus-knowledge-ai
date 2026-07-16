import streamlit as st

from src.agente import AgentePegasus


# -------------------------------------------------------
# Configuración
# -------------------------------------------------------

st.set_page_config(
    page_title="Pegasus Agente Empresarial",
    page_icon="🦄",
    layout="centered"
)

# -------------------------------------------------------
# Título
# -------------------------------------------------------

st.title("Pegasus Agente Empresarial")

st.write("")

# -------------------------------------------------------
# Consulta
# -------------------------------------------------------

pregunta = st.text_input(
    "¿Qué información necesitas?",
    placeholder="Escribe tu consulta..."
)

# -------------------------------------------------------
# Botón
# -------------------------------------------------------

if st.button("Consultar", use_container_width=True):

    if pregunta.strip():

        with st.spinner("Consultando..."):

            agente = AgentePegasus()

            documentos = agente.retriever.buscar(pregunta)

            prompt = agente.prompt_builder.construir(
                pregunta,
                documentos
            )

            respuesta = agente.llm.generar_respuesta(prompt)

        st.divider()

        st.write(respuesta)