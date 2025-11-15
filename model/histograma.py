import yfinance as yf
import pandas as pd
import altair as alt
import streamlit as st

# Obtener datos rápidos
datos = yf.download("AAPL", period="3y")
datos = datos.reset_index().rename(columns={'Date': 'date'})

# Gráfico OHLC simple
chart = alt.Chart(datos).mark_rule().encode(
    x='date:T',
    y='Low:Q',
    y2='High:Q',
    color=alt.condition("datum.Open <= datum.Close", alt.value("green"), alt.value("red"))
) + alt.Chart(datos).mark_bar().encode(
    x='date:T',
    y='Open:Q',
    y2='Close:Q',
    color=alt.condition("datum.Open <= datum.Close", alt.value("green"), alt.value("red"))
).properties(
    title='Gráfico OHLC - AAPL (1 mes)',
    width=600, 
    height=400
)

# Mostrar en Streamlit
st.altair_chart(chart, use_container_width=True)

# También mostrar los datos en tabla
st.write("### Datos OHLC")
st.dataframe(datos)