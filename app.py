import streamlit as st

# =====================================================
# CONFIGURACIÓN DE LA PÁGINA
# =====================================================

st.set_page_config(
    page_title="Pegasus Agente Empresarial",
    page_icon="🤖",
    layout="centered"
)

# =====================================================
# TÍTULO
# =====================================================

st.title("🤖 Pegasus Agente Empresarial")

# =====================================================
# CONSULTA
# =====================================================

pregunta = st.text_input(
    "¿Qué información necesitas?",
    placeholder="Escribe tu consulta..."
)

# =====================================================
# BOTÓN
# =====================================================

if st.button("Consultar", use_container_width=True):

    st.info("Aquí aparecerá la respuesta del agente.")