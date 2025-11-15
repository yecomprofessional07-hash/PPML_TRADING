#================================= Importaciones/Librerías ================================#
import streamlit as st
import pandas as pd

#=================================== Variables Globales ===================================#
userName = "user"                           # Valor dinámico: nombre de usuario
budget = 0                                  # Valor dinámico: presupuesto del usuario
moneyInStocks = 0                           # Valor dinámico: dinero invertido en acciones
image = 1                                   # Valor dinámico: imagen de perfil del usuario
df = pd.DataFrame()                         # Valor dinámico: DataFrame con información del usuario

#=============================== Configuración de la página ===============================#
st.set_page_config(page_title="Gestor de Trading Basado en ML", layout="centered")

#====================================== Contenido principal ======================================#
# Primera fila: Título
st.markdown(f"<h1 style='text-align: center;'>GESTOR DE TRADING BASADO EN ML</h1>", unsafe_allow_html=True)

# Separador
st.markdown("---")

# Segunda fila: Información del usuario
col1, col2, col3 = st.columns([2, 0.5, 2])
with col1:
    # Primera columna: Imagen de perfil
    st.image(f"sources/profileImage{image}.png", width=280)
with col3:
    # Segunda columna: Información del usuario
    st.markdown(f"### {userName}")
    st.markdown(f"####")
    st.metric(label="PRESUPUESTO", value=f"{budget}")
    st.metric(label="DINERO EN ACCIONES", value=f"{moneyInStocks}")

# Separador
st.markdown("---")



# Separador
st.markdown("---")

# Tercera fila: Edición de configuraciónes
if st.button("Agregar Presupuesto", use_container_width=True):
    with st.container(border=True):
        newBudget = st.number_input("Monto a agregar", min_value=1000.00, value=1500.00, format="%.2f", step=1.00)
        if st.button("Confirmar"):
            budget += newBudget
            st.success(f"Se han agregado L. {newBudget} a su presupuesto.")
            st.experimental_rerun()

# Separador
st.markdown("---")

# botón para volver a principal.py
if st.button("Volver", use_container_width=True):
    st.switch_page("pages/principal.py")