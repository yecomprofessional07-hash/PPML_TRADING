import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Gestor de Trading", layout="wide")

# --- SIDEBAR IZQUIERDA ---
with st.sidebar:
    # Perfil y logout
    col1, col2 = st.columns([4, 1])
    with col1:
        st.image("https://via.placeholder.com/80x80.png?text=Perfil", width=60)
        st.markdown("**username**")
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
    st.button("Información", key="info")
    st.button("Configuración", key="config")

#Contenido principal
col_main, col_actions = st.columns([4, 1])

with col_main:
    st.markdown("## GESTOR DE TRADING BASADO EN MACHINE LEARNING")
    
    # Histograma
    
    # Métricas
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="Métrica 1", value=f"---")
    with col_m2:
        st.metric(label="Métrica 2", value=f"---")
    with col_m3:
        st.metric(label="Métrica 3", value=f"---")

#Botones de acción
with col_actions:
    st.markdown("### Botones de Acción")
    st.button("Comprar", use_container_width=True)
    st.button("Vender", use_container_width=True)
    st.button("Mantener", use_container_width=True)