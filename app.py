import streamlit as st
import pandas as pd

# --- Configuración general ---
st.set_page_config(
    page_title="Gestor de Trading basado en ML",
    layout="centered"
)

st.markdown("""
    <style>
        section[data-testid="stMain"] {
            overflow: hidden !important;
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([4, 10, 4])
with col2:
    with st.container(border = True):
        # Título
        st.markdown(
            "<h3 style='text-align: center;'>GESTOR DE TRADING BASADO EN ML</h3>",
            unsafe_allow_html=True
        )

        st.write("---")

        # Imputs de usuario
        usuario = st.text_input("Usuario", placeholder="Ingrese su usuario")
        st.write("")
        contraseña = st.text_input("Contraseña", type="password", placeholder="Ingrese su contraseña")
        st.write("")
        st.write("")

        # Botón de inicio de sesión
        login_btn = st.button("Iniciar sesión", type="primary", use_container_width=True)

        # Lógica de autenticación
        if login_btn:
            if usuario and contraseña:
                st.success(f"¡Bienvenido!, {usuario}")
            else:
                st.error("Por favor, ingrese usuario y contraseña.")

        st.write("---")

        st.write("¿No tienes cuenta? [Regístrate.](https://google.com)")