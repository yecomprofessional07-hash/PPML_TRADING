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
""",
unsafe_allow_html=True)

# Creamos un contenedor vacío para mostrar el mensaje de error del monto
# Esto permite que el error esté arriba del botón.
error_placeholder = st.empty() 

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
        monto = st.text_input ("Monto Inicial",placeholder="Ingrese un monto inicial (solo números)" )
 
        st.write("")
 
        st.write("")
 
 
        # Botón de inicio de sesión
        login_btn = st.button("Registrar Usuario", type="primary", use_container_width=True)
 
        # Lógica de autenticación
        if login_btn:
            # Limpiamos cualquier error anterior
            error_placeholder.empty()

            # 1. Validación de campos obligatorios
            if not user or not password:
                error_placeholder.error("Por favor, ingrese usuario y contraseña.")
            else:
                # 2. Validación de que el MONTO es numérico
                try:
                    # Intenta convertir el monto a un número (float)
                    monto_numerico = float(monto)
                    
                    # Si la conversión es exitosa:
                    # Si tu compañero no ha creado 'principal.py' o no funciona,
                    # puedes cambiar la siguiente línea por un mensaje de éxito temporal:
                    # st.success("¡Validación exitosa! Monto es un número. (Falta la conexión a principal.py)")
                    st.switch_page("principal.py") 

                except ValueError:
                    # Si falla la conversión (significa que hay letras o símbolos no numéricos)
                    error_placeholder.error("⚠️ Error en 'Monto Inicial': Por favor, ingrese solo números.")
 
        # Separador
        st.write("---")