#================================= Importaciones/Librerías ================================#
import streamlit as st
import pandas as pd
import random
import yfinance as yf
import altair as alt
# Importa solo de B.
from model.solicitudes import manejar_dato_para_a




#====================###DICCIONARIOS###====================#

dicc_tiempo ={
    '1 Mes':'1mo', '3 Meses':'3mo', '6 Meses':'6mo', 
    '1 Año':'1y', '5 Años':'5y', '10 Años':'10y', 
    '20 Años':'20y'
}
empresas = {
    # 🔴 TECNOLOGÍA (25 empresas)
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Meta Platforms (Facebook)": "META",
    "Tesla": "TSLA",
    "Broadcom": "AVGO",
    "Adobe": "ADBE",
    "Salesforce": "CRM",
    "Oracle": "ORCL",
    "Cisco": "CSCO",
    "Intel": "INTC",
    "IBM": "IBM",
    "Qualcomm": "QCOM",
    "AMD": "AMD",
    "Netflix": "NFLX",
    "PayPal": "PYPL",
    "Intuit": "INTU",
    "ServiceNow": "NOW",
    "Applied Materials": "AMAT",
    "Texas Instruments": "TXN",
    "Micron Technology": "MU",
    "Snowflake": "SNOW",
    "Shopify": "SHOP",
    
    # 🏦 FINANZAS (20 empresas)
    "JPMorgan Chase": "JPM",
    "Bank of America": "BAC",
    "Wells Fargo": "WFC",
    "Citigroup": "C",
    "Goldman Sachs": "GS",
    "Morgan Stanley": "MS",
    "BlackRock": "BLK",
    "Visa": "V",
    "Mastercard": "MA",
    "American Express": "AXP",
    "S&P Global": "SPGI",
    "Moody's": "MCO",
    "Blackstone": "BX",
    "Charles Schwab": "SCHW",
    "PNC Financial": "PNC",
    "Truist Financial": "TFC",
    "US Bancorp": "USB",
    "Capital One": "COF",
    "Aon": "AON",
    "Marsh & McLennan": "MMC",
    
    # 🏥 SALUD (15 empresas)
    "Johnson & Johnson": "JNJ",
    "UnitedHealth": "UNH",
    "Pfizer": "PFE",
    "Merck": "MRK",
    "AbbVie": "ABBV",
    "Eli Lilly": "LLY",
    "Thermo Fisher Scientific": "TMO",
    "Abbott Laboratories": "ABT",
    "Danaher": "DHR",
    "Amgen": "AMGN",
    "Bristol-Myers Squibb": "BMY",
    "Gilead Sciences": "GILD",
    "Moderna": "MRNA",
    "Regeneron": "REGN",
    "Biogen": "BIIB",
    
    # 🛒 CONSUMO (20 empresas)
    "Procter & Gamble": "PG",
    "Walmart": "WMT",
    "Coca-Cola": "KO",
    "PepsiCo": "PEP",
    "McDonald's": "MCD",
    "Nike": "NKE",
    "Home Depot": "HD",
    "Lowe's": "LOW",
    "Starbucks": "SBUX",
    "Costco": "COST",
    "Target": "TGT",
    "Disney": "DIS",
    "Netflix": "NFLX",
    "Booking Holdings": "BKNG",
    "Estée Lauder": "EL",
    "Colgate-Palmolive": "CL",
    "Mondelez": "MDLZ",
    "Kraft Heinz": "KHC",
    "General Mills": "GIS",
    "Hershey": "HSY",
    
    # ⚡ ENERGÍA/INDUSTRIALES (10 empresas)
    "Exxon Mobil": "XOM",
    "Chevron": "CVX",
    "ConocoPhillips": "COP",
    "NextEra Energy": "NEE",
    "Southern Company": "SO",
    "Boeing": "BA",
    "Caterpillar": "CAT",
    "3M": "MMM",
    "Honeywell": "HON",
    "Union Pacific": "UNP",
    
    # 🏠 BIENES RAÍCES/UTILIDADES (10 empresas)
    "American Tower": "AMT",
    "Crown Castle": "CCI",
    "Prologis": "PLD",
    "Equinix": "EQIX",
    "Digital Realty": "DLR",
    "Verizon": "VZ",
    "AT&T": "T",
    "T-Mobile": "TMUS",
    "Comcast": "CMCSA",
    "Charter Communications": "CHTR"
}

#=================================== Variables Globales ===================================#


userName = "user"                           # Valor dinámico: nombre de usuario
budget = 0                                  # Valor dinámico: presupuesto del usuario
moneyInStocks = 0                           # Valor dinámico: dinero invertido en acciones
df = pd.DataFrame()                         # Valor dinámico: DataFrame para almacenar los datos del histograma

#=============================== Funciones para los botones =============?=================#
# Función para la ventana emergente
def popUp():
    pass

# Función para el botón de comprar
def buyActions():
    st.toast("Has comprado acciones con éxito.")

# Función para el botón de vender
def sellActions():
    st.toast("Haz vendido tus acciones con éxito.")

# Función para el botón de mantener
def standBy(): 
    st.toast("Has decidido mantener tus acciones.")

#=============================== Configuración de la página ===============================#
st.set_page_config(page_title="Gestor de Trading", layout="wide")

#====================================== Barra lateral =====================================#
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
    busqueda = st.text_input("Buscar por nombre:", placeholder="Escribe un nombre...",key="Busqueda")
    if not busqueda in empresas.keys():
        st.markdown("Acción no Registrada")
    # Acción/es en uso
    accion = st.multiselect("Acciones en uso", ['AAPL','GOOG','AMZN','TSLA','META'], default='AAPL')

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
iniciar = ''

if accion:
    iniciar = accion
elif busqueda in empresas.keys():
    iniciar = empresas[busqueda]


#Segunda fila: Histograma + botones de acción
col1, col2 = st.columns([4, 1])
with col1:
    # Histograma
    
    if time in dicc_tiempo.keys():
        periodo = dicc_tiempo[time]
    else:
        periodo = '6mo'
    if not iniciar == '':
        datos = yf.download(iniciar, period=periodo)
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
            title=f'Gráfico OHLC - ({time} )',
            width=600, 
            height=400
        )
        
        st.altair_chart(chart, use_container_width=True)
    else:
        st.write("### No tienes acciones en uso")
    # Mostrar en Streamlit
    

    # También mostrar los datos en tabla
    #st.write("### Datos OHLC")
    #st.dataframe(datos)
    st.line_chart(df, use_container_width=True)
with col2:
    #Botones de acción
    st.markdown("#### Botones de Acción")
    if st.button("Comprar", use_container_width=True):
        buyActions()
    if st.button("Vender", use_container_width=True):
        sellActions()
    if st.button("Mantener", use_container_width=True):
        standBy()

st.markdown("---")

#================Funciones para metricas================#
def iniciar_proceso():
    if iniciar == '':
        dato_inicial = 'AAPL'
    else: 
        dato_inicial = iniciar
    # Llama a B para que maneje el proceso
    dato_final = manejar_dato_para_a(dato_inicial)
    
    #print(f"A: Proceso completado. Resultado final: {dato_final}")
    return dato_final
decision, confianza, precio = iniciar_proceso()     # Valores dinámicos: se importa el ML y con una función se obtienen los valores de métricas


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

#==============Funciones de envio=========#


def buscador():
    if busqueda in empresas.keys():
        return busqueda