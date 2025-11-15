#================================== Importaciones/Librerías ==================================#
import streamlit as st
import pandas as pd
import random
from model.solicitudes import recibir

#================================== Variables Globales ==================================#

decision, confianza, precio = recibir()     # Valores dinámicos: se importa el ML y con una función se obtienen los valores de métricas
userName = "user"                           # Valor dinámico: nombre de usuario
budget = 0                                  # Valor dinámico: presupuesto del usuario
moneyInStocks = 0                           # Valor dinámico: dinero invertido en acciones
df = pd.DataFrame()                         # Valor dinámico: DataFrame para almacenar los datos del histograma

#=============================== Configuración de la página ===============================#
st.set_page_config(page_title="Gestor de Trading", layout="wide")

#====================================== Barra lateral ======================================#
# Sidebar: Información del usuario (Nombre de usuario, foto de perfil, horizonte de tiempo, multiselectbox de acciones, presupuesto y acciones en uso) + botones relevantes (acerca de, tema, cerrar sesión, botón de función indeterminada)
with st.sidebar:
    # Perfil y logout
    col1, col2 = st.columns([4, 1])
    with col1:
        colSub1, colSub2 = st.columns([5, 15])
        with colSub1:
            st.image(f"sources/profileImage{random.randint(1,3)}.png", width=40)
        with colSub2:
            st.markdown(f"#### **{userName}**")
    with col2:
        def logout():
            st.switch_page("app.py")
            
        st.button("←", key="logout", help="Cerrar sesión")
    
    st.markdown("---")
    
    # Acción/es en uso
    accion = st.multiselect("Acciones en uso", ['AAPL','GOOG','AMZN','TSLA','META'], default=['AAPL'])

    # Horizonte de tiempo
    time = st.pills("Horizonte de tiempo", ['1 Mes', '3 Meses', '6 Meses', '1 Año', '5 Años', '10 Años', '20 Años'], default="6 Meses",)

    st.markdown("---")

    # Presupuesto
    st.markdown("#### Presupuesto")
    st.markdown(f"L. {budget:,}")
    
    # Dinero en acciones
    st.markdown("#### Dinero en Acciones")
    st.markdown(f"L. {moneyInStocks:,}")
    
    st.markdown("---")
    
    # Botones inferiores
    st.button("Acerca de", key="info", use_container_width=True)
    st.button("Configuración", key="config", use_container_width=True)

#====================================== Contenido principal ======================================#
#Primera fila: Título
st.markdown("## GESTOR DE TRADING BASADO EN MACHINE LEARNING")

st.markdown("---")

#Segunda fila: Histograma + botones de acción
col1, col2 = st.columns([4, 1])
with col1:
    # Histograma
    st.line_chart(df, use_container_width=True)
with col2:
    #Botones de acción
    st.markdown("#### Botones de Acción")
    st.button("Comprar", use_container_width=True)
    st.button("Vender", use_container_width=True)
    st.button("Mantener", use_container_width=True)

st.markdown("---")

#Tercera fila: Métricas
col1, col2, col3 = st.columns(3)
with col1:
    # Métrica 1
    st.metric(label="DECISIÓN DEL MODELO", value=f"{decision}")
with col2:
    # Métrica 2
    st.metric(label="CONFIANZA", value=f"{confianza:.2%}")
with col3:
    # Métrica 3
    st.metric(label="Precio actual", value=f"{precio:.2f}")