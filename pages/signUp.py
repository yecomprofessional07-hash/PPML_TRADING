# Librerías
import streamlit as st
import pandas as pd
import random

# Configuración de la página
st.set_page_config(page_title="Gestor de Trading Basado en ML", layout="centered")

#=======Diccionarios=====#
image = random.randint(1, 3)


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
        user = st.text_input("Nuevo Usuario", placeholder="Ingrese su nuevo usuario")
        # Espaciado
        st.write("")
 
        # Input: password
        password = st.text_input("Nueva Contraseña", type="password", placeholder="Ingrese su nueva contraseña")
        # Espaciado
        st.write("")

        # Entrada de capital
        monto = st.number_input("Monto Inicial", min_value=1000.00, value=1500.00, format="%.2f", step=1.00)
        

        # Espaciado
        st.write("")
        st.write("")
 
        # Lógica de autenticación
        if st.button("Registrar Usuario", type="primary", use_container_width=True):
            # 1. Validación de campos obligatorios
            if not user or not password:
                st.toast("Por favor, ingrese usuario y contraseña.")
            else:
                # 2. Validación de que el MONTO es numérico
                try:
                    # Intenta convertir el monto a un número (float)
                    monto_numerico = float(monto)
                    st.session_state['nuevo_usuario'] = user
                    st.session_state['monto_inicial'] = monto_numerico
                    
                    #agregando dataframe

                    df = pd.read_csv('data/users.csv')
                    ident = len(df)+1
                    # Crear lista

                    lista_usuario = [user, password, monto, image,ident]
        
    
                    nueva_fila = {'user': lista_usuario[0], 'password': lista_usuario[1], 
                                  'monto':lista_usuario[2], 'image':lista_usuario[3],'identidad':lista_usuario[4]}
                    
                    for col in df.columns[5:]:
                        nueva_fila[col] = 0
                    
                    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
                    df.to_csv('data/users.csv', index=False)
                    st.session_state['identidad'] = ident
                    st.success(f"✅ Usuario {lista_usuario[0]} creado exitosamente!")
                    # Si la conversión es exitosa:
                    st.switch_page("pages/principal.py") 
                except ValueError:
                    # Si falla la conversión (significa que hay letras o símbolos no numéricos)
                    st.toast("Por favor, ingrese solo números.")

        # Separador
        st.write("---")

        # Enlace de registro
        subcol1, subcol2 = st.columns([1, 1])
        with subcol1:
            st.write("¿Ya tienes una cuenta?")
        with subcol2:
            st.page_link("app.py", label="Inicia sesión.")
