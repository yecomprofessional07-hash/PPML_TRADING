import streamlit as st
import pandas as pd
from backend.acciones.solicitudes import recibie


#He importado el ML y colocado en las metricas
decision, confianza, precio = recibie()


#He agregado esta funcion con el objetivo de proporcionar
# el csv users el cual contiene usersname y password



# Configuración de la página
st.set_page_config(page_title="Gestor de Trading", layout="wide")

# Sidebar: Información del usuario (Nombre de usuario, foto de perfil, presupuesto y acciones en uso) + botones relevantes (acerca de, tema, cerrar sesión, botón de función indeterminada)
with st.sidebar:
    # Perfil y logout
    col1, col2 = st.columns([4, 1])
    with col1:
        colSub1, colSub2 = st.columns([5, 15])
        with colSub1:
            st.image("sources/xd.jpg", width=50)
        with colSub2:
            st.markdown("#### **user**")
    with col2:
        st.button("←", key="logout", help="Cerrar sesión")
    
    st.markdown("---")
    
    # Acción en uso
    st.markdown("#### Acción en uso")
    accion = st.selectbox("Selecciona acción", ["action1", "action2", "action3", "action4"], label_visibility="collapsed")
    
    # Presupuesto y dinero en acciones
    st.markdown("#### Presupuesto")
    presupuesto = 0  # valor dinámico
    st.markdown(f"L. {presupuesto:,}")
    
    st.markdown("#### Dinero en Acciones")
    dinero_acciones = 0  # valor dinámico
    st.markdown(f"L. {dinero_acciones:,}")
    
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
    pass
#Botones de acción
with col_actions:
    #Botones de acción
    st.markdown("### Botones de Acción")
    st.button("Comprar", use_container_width=True)
    st.button("Vender", use_container_width=True)
    st.button("Mantener", use_container_width=True)

st.markdown("---")

#Tercera fila: Métricas
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
        st.metric(label="🎯 DECISIÓN DEL MODELO", value=f"{decision}")
with col_m2:
    st.metric(label="📊 CONFIANZA", value=f"{confianza:.2%}")
with col_m3:
    st.metric(label="💰 Precio actual", value=f"{precio:.2f}")