import streamlit as st
import pandas as pd


# --- Configuración general de la página ---
st.set_page_config(
    page_title="Login - Gestor de Trading basado en ML",
    page_icon="💹",
    layout="centered"
)

# --- Estilos personalizados ---
st.markdown("""
    <style>
    body {
        background-color: #e6f0ff; /* Azul suave */
    }
    .main {
        background-color: #e6f0ff;
    }
        h1{text-align: center;}margin-top:0px;margin-bottom:20px;}         #nuevo
        stTextInput label{text-align:center; display:block; width:100%;}
            
    .login-container {
        background-color: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        text-align: center;
        width: 350px;
        margin: auto;
    }
    h1 {
        color: #003366;
        margin-bottom: 25px;
    }
    label, p {
        color: #003366;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        text-align: center;
    }
    .forgot {
        color: #3366cc;
        font-size: 14px;
        margin-bottom: 25px;
        cursor: pointer;
    }
    .register {
        color: #003366;
        margin-top: 20px;
        font-size: 14px;
    }
    .register a {
        color: #0047b3;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- Contenido de la página ---
with st.container():
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)

    st.markdown("<h1>Gestor de Trading basado en ML</h1>", unsafe_allow_html=True)

    # Campo de usuario
    usuario = st.text_input("Usuario", placeholder="Ingrese su usuario")

    # Campo de contraseña
    contraseña = st.text_input("Contraseña", type="password", placeholder="Ingrese su contraseña")

    # Texto de olvidó contraseña
    st.markdown("<p class='forgot'>¿Olvidó su contraseña?</p>", unsafe_allow_html=True)

    # Botón de login
    login_btn = st.button("LOGIN")

    if login_btn:
        if usuario and contraseña:
            st.success(f"Bienvenido, {usuario} 👋")
        else:
            st.error("Por favor, ingrese usuario y contraseña.")

    # Texto de registro
    st.markdown(
        "<p class='register'>¿No tienes una cuenta? <a href='#'>Regístrate</a></p>",
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)
