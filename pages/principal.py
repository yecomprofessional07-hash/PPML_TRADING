#================================== Importaciones/Librerías ==================================#
import streamlit as st
import pandas as pd
import random
from model.solicitudes import recibir

#================================== Variables Globales ==================================#
decision, confianza, precio = recibir() #He importado el ML y colocado en las metricas
userName = "user"   # valor dinámico: nombre de usuario
budget = 0          # valor dinámico: presupuesto del usuario
moneyInStocks = 0   # valor dinámico: dinero invertido en acciones
df = pd.DataFrame() # DataFrame para almacenar los datos del histograma

#He agregado esta funcion con el objetivo de proporcionar
#el csv users el cual contiene usersname y password

#=============================== Configuración de la página ===============================#
st.set_page_config(page_title="Gestor de Trading", layout="wide")

#====================================== Barra lateral ======================================#
# Sidebar: Información del usuario (Nombre de usuario, foto de perfil, presupuesto y acciones en uso) + botones relevantes (acerca de, tema, cerrar sesión, botón de función indeterminada)
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
    
    # Acción en uso
    accion = st.multiselect("Acciones en uso", ['AAPL','GOOG','AMZN','TSLA','META'], default=['AAPL'])

    # Horizonte de tiempo
    time = st.pills("Horizonte de tiempo", ['1 Mes', '3 Meses', '6 Meses', '1 Año', '5 Años', '10 Años', '20 Años'], default="6 Meses",)

    st.markdown("---")

    # Presupuesto y dinero en acciones
    st.markdown("#### Presupuesto")
    st.markdown(f"L. {budget:,}")
    
    st.markdown("#### Dinero en Acciones")
    st.markdown(f"L. {moneyInStocks:,}")
    
    st.markdown("---")
    
    # Botones inferiores
    tema_switch = st.toggle("Cambiar Tema", key="tema")
    st.button("Acerca de", key="info", use_container_width=True)
    st.button("Configuración", key="config", use_container_width=True)

#====================================== Contenido principal ======================================#
#Primera fila: Título
st.markdown("## GESTOR DE TRADING BASADO EN MACHINE LEARNING")

st.markdown("---")

#Segunda fila: Histograma + botones de acción
col_histograma, col_actions = st.columns([4, 1])
with col_histograma:
    # Histograma
    st.line_chart(df, use_container_width=True)

#Botones de acción
with col_actions:
    #Botones de acción
    st.markdown("#### Botones de Acción")
    st.button("Comprar", use_container_width=True)
    st.button("Vender", use_container_width=True)
    st.button("Mantener", use_container_width=True)

st.markdown("---")

#Tercera fila: Métricas
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
        st.metric(label="DECISIÓN DEL MODELO", value=f"{decision}")
with col_m2:
    st.metric(label="CONFIANZA", value=f"{confianza:.2%}")
with col_m3:
    st.metric(label="Precio actual", value=f"{precio:.2f}")