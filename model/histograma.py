import yfinance as yf
import pandas as pd
import altair as alt
import streamlit as st

data = pd.DataFrame({
    'nombre': ['Ana Gómez', 'Carlos López', 'María Rodríguez', 'Pedro Sánchez'],
    'edad': [25, 32, 28, 45],
    'ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
    'salario': [30000, 45000, 35000, 50000]
})

# Búsqueda simple
st.title("🔍 Búsqueda Básica")

busqueda = st.text_input("Buscar por nombre:", placeholder="Escribe un nombre...")

if busqueda:
    resultados = data[data['nombre'].str.contains(busqueda, case=False, na=False)]
    st.write(f"**Resultados para '{busqueda}':**")
    st.dataframe(resultados)
else:
    st.dataframe(data)