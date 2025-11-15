# Librerías
import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Registro", layout="centered")

# CSS para ocultar la barra de desplazamiento horizontal
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
            "<h3 style='text-align: center;'>Registro de nuevo usuario ML</h3>",
            unsafe_allow_html=True
        )

        # Separador
        st.write("---")

        # Imput: user
        user = st.text_input("Nuevo Usuario", placeholder="Ingrese su nuevo usuario")
        # Espaciado
        st.write("")

        password = st.text_input("Nueva Contraseña", type="password", placeholder="Ingrese su nueva contraseña")
        # Espaciado
        # Entrada de capital
        monto=  st.text_input ("Monto Inicial",placeholder="Ingrese un monto inicial" )
        st.write("")
        st.write("")

        # Botón de inicio de sesión
        login_btn = st.button("Registrar Usuario", type="primary", use_container_width=True)

        # Lógica de autenticación
        if login_btn:
            if user and password:
                st.switch_page("principal.py")
            else:
                st.error("Por favor, ingrese usuario y contraseña.")

        # Separador
        st.write("---")

       