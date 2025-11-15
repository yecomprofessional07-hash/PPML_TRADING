import streamlit as st
import pandas as pd

# --- Configuración general ---
st.set_page_config(
    page_title="Login - Gestor de Trading basado en ML",
    page_icon="💹",
    layout="centered"
)


# --- Contenedor central sin HTML ---
with st.container():
    # Centrado: usamos columnas vacías
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("## Gestor de Trading basado en ML")

        # Tarjeta simulada con Streamlit
        with st.container(border=True):
            
            usuario = st.text_input("Usuario", placeholder="Ingrese su usuario")
            contraseña = st.text_input("Contraseña", type="password", placeholder="Ingrese su contraseña")
            
            st.write("")  # Espacio
            
            st.button("¿Olvidó su contraseña?")

            login_btn = st.button("LOGIN")

            if login_btn:
                if usuario and contraseña:
                    st.success(f"Bienvenido, {usuario} 👋")
                else:
                    st.error("Por favor, ingrese usuario y contraseña.")

            st.write("---")

            st.write("¿No tienes una cuenta?")
            st.link_button("Regístrate", "#")