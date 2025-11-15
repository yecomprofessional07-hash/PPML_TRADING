#================================= Importaciones/Librerías ================================#
import streamlit as st
import pandas as pd

#=================================== Variables Globales ===================================#
userName = "user"                           # Valor dinámico: nombre de usuario
budget = 0                                  # Valor dinámico: presupuesto del usuario
moneyInStocks = 0                           # Valor dinámico: dinero invertido en acciones
image = 1                                   # Valor dinámico: imagen de perfil del usuario

#=============================== Configuración de la página ===============================#
st.set_page_config(page_title="Gestor de Trading Basado en ML", layout="centered")

#====================================== Contenido principal ======================================#