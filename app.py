# Librerías
import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Gestor de Trading Basado en ML", layout="centered")
df = pd.read_csv("data/users.csv")
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
            "<h3 style='text-align: center;'>GESTOR DE TRADING BASADO EN ML</h3>",
            unsafe_allow_html=True
        )

        # Separador
        st.write("---")

        # Imput: user
        user = st.text_input("Usuario", placeholder="Ingrese su usuario")
        # Espaciado
        st.write("")

        password = st.text_input("Contraseña", type="password", placeholder="Ingrese su contraseña")
        # Espaciado
        st.write("")
        st.write("")

        # Botón de inicio de sesión
        login_btn = st.button("Iniciar sesión", type="primary", use_container_width=True)

        # Lógica de autenticación
        if login_btn:
            if user in df['user'].values:
                fila_usuario = df[df['user'] == user]
                if not fila_usuario.empty and fila_usuario.iloc[0]['password'] == password:
                    st.session_state['usuario_registrado'] = user
                    st.switch_page("pages/principal.py")
                    
                else:
                    st.error("Credenciales no válidas")
            else:
                st.toast("Por favor, ingrese usuario y contraseña.")

        # Separador
        st.write("---")

        # Enlace de registro
        subcol1, subcol2 = st.columns([1, 1])
        with subcol1:
            st.write("¿No tienes una cuenta?")
        with subcol2:
            st.page_link("pages/signUp.py", label="Regístrate.")