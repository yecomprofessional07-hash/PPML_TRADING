import streamlit as st
import pandas as pd
import pathlib 

#He agregado esta funcion con el objetivo de proporcionar
# el csv users el cual contiene usersname y password
#importe pathlib para darle la ruta a la funcion pd.read_csv

def cargar_csv(nombre_archivo):
    """Carga CSV desde data/ independientemente de dónde se ejecute"""
    proyecto_root = pathlib.Path(__file__).parent.parent.parent # Subir a PPML_TRADING
    ruta_csv = proyecto_root / 'data' / nombre_archivo
    print(f"Intentando cargar archivo desde: {ruta_csv}")
    return pd.read_csv(ruta_csv)
datos = cargar_csv("users.csv")
print(datos)


# Uso
#df = cargar_csv('empresas.csv')
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
            usuario_validado = datos[(datos['username']==usuario) & 
                                     (datos['password'].astype(str)==contraseña)]
            if not usuario_validado.empty:
                st.success(f"Bienvenido, {usuario} 👋")
            else:
                st.error("Usuario o contraseña invalidos")
        else:
            st.error("Por favor, ingrese Usuario y Contraseña")

    # Texto de registro
    st.markdown(
        "<p class='register'>¿No tienes una cuenta? <a href='#'>Regístrate</a></p>",
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)
