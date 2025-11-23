#================================= Importaciones/Librerías ================================#
import streamlit as st
import pandas as pd
import time

#=================================== Variables Globales ===================================#
df = pd.read_csv("data/users.csv")
#columnas_positivas = []

if 'identidad' in st.session_state:
    id = st.session_state['identidad']
    fila_usuario = df[df['identidad'] == id]
    budget = fila_usuario.iloc[0]['monto']
    moneyInStocks = fila_usuario.iloc[0]['acciones']
    userName = fila_usuario.iloc[0]['user']
    image = fila_usuario.iloc[0]['image']
#=============================== Configuración de la página ===============================#
st.set_page_config(page_title="Gestor de Trading Basado en ML", layout="centered")
#for col in df.columns[6:]:
    #if fila_usuario.iloc[0][col] > 0:
       # columnas_positivas.append(col)

#palabras = " ".join(columnas_positivas)

#====================================== Contenido principal ======================================#
# ---> Primera fila: Título
st.markdown(f"<h1 style='text-align: center;'>GESTOR DE TRADING BASADO EN ML</h1>", unsafe_allow_html=True)

# Separador
st.markdown("---")

# --->Segunda fila: Información del usuario
col1, col2, col3 = st.columns([2, 0.5, 2])
with col1:
    # Primera columna: Imagen de perfil
    st.image(f"sources/profileImage{image}.png", width=280)
with col3:
    # Segunda columna: Información del usuario
    st.markdown(f"### {userName}")
    st.markdown(f"####")
    st.metric(label="PRESUPUESTO", value=f"{budget:,.2f}")
    st.metric(label="DINERO EN ACCIONES", value=f"{moneyInStocks:,.2f}")

# Separador
st.markdown("---")

st.markdown(f"#### Lista de empresas en su portafolio:")

# Separador
st.markdown("---")

# ---> Tercera fila: Edición de configuraciónes
# Inicializa la variables de sesión para mostrar/ocultar los contenedores
if "show_containerBudget" not in st.session_state:
    st.session_state.show_containerBudget = False
if "show_containerName" not in st.session_state:
    st.session_state.show_containerName = False

# Botón para mostrar/ocultar el contenedor de agregar presupuesto
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Agregar presupuesto", use_container_width=True, key="btnBudget"):
        st.session_state.show_containerBudget = not st.session_state.show_containerBudget
with col2:
    if st.button("Cambiar nombre", use_container_width=True, key="btnName"):
        st.session_state.show_containerName = not st.session_state.show_containerName
with col3:
    if st.button("Función Experimental", use_container_width=True, key="btnExperimental"):
        pass

if st.session_state.show_containerBudget:
    with st.container(border=True):
        # Spinbox que permite agregar presupuesto
        newBudget = st.number_input("Monto a agregar", min_value=1000.00, value=1500.00, format="%.2f", step=1.00)
        if st.button("Confirmar", key="confirmBudget"):
            # Actualiza el presupuesto
            budget += newBudget
            df.loc[df['user'] == userName, 'monto'] = budget
            df.to_csv('data/users.csv', index=False)
            # Muestra un mensaje de éxito
            st.success(f"Se han agregado L. {newBudget} a su presupuesto.")

            # Oculta el contenedor después de confirmar
            st.session_state.show_containerBudget = False

            # Espera un segundo y vuelve a cargar la página para actualizar los valores
            time.sleep(1)
            st.rerun()

if st.session_state.show_containerName:
    with st.container(border=True):
        # Campo de texto para cambiar el nombre de usuario
        newName = st.text_input("Ingrese su nuevo nombre de usuario", max_chars=20)

        if st.button("Confirmar", key="confirmName"):
            if newName.strip() != "":
                # Actualiza el nombre de usuario
                df.loc[df['identidad'] == id, 'user'] = newName
                df.to_csv('data/users.csv', index=False)
                # Muestra un mensaje de éxito
                st.success(f"Su nombre de usuario ha sido cambiado a {newName}.")

                # Oculta el contenedor después de confirmar
                st.session_state.show_containerName = False

                # Espera un segundo y vuelve a cargar la página para actualizar los valores
                time.sleep(1)
                st.rerun()
            else:
                st.warning("El nombre de usuario no puede estar vacío.")

# Separador
st.markdown("---")

# ---> Cuarta fila
# botón para volver a principal.py
if st.button("Volver", use_container_width=True):
    st.switch_page("pages/principal.py")
