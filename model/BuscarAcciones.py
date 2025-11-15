
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
#from .solicitudes import envio
#from .solicitudes import enviar

# modulo_c.py

def procesar_dato(dato):
    """Simula el procesamiento del dato."""
    print(f"C: Procesando dato: {dato}")
    dato_procesado = dato


    # 1. Descargar datos
    empresa = dato_procesado

    datos = yf.download(empresa, period='2y')

    # 2. Calcular RSI
    def calcular_rsi(precios, window=14):
        delta = precios.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    # 3. Crear características
    datos['SMA_20'] = datos['Close'].rolling(20).mean()
    datos['RSI'] = calcular_rsi(datos['Close'])
    datos['Volatility'] = datos['Close'].rolling(20).std()

    # 4. Crear variable objetivo (Compra=2, Hold=1, Vender=0)
    datos['Future_Return'] = datos['Close'].shift(-5) / datos['Close'] - 1
    datos['Decision'] = datos['Future_Return'].apply(
        lambda x: 2 if x > 0.02 else 0 if x < -0.01 else 1
    )

    # 5. Preparar datos para entrenamiento
    datos_limpios = datos.dropna()
    X = datos_limpios[['SMA_20', 'RSI', 'Volatility']]
    y = datos_limpios['Decision']

    # 6. Entrenar modelo
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    modelo = LogisticRegression(random_state=42)
    modelo.fit(X_scaled, y)

    print("✅ Modelo entrenado!")

    # Obtener los datos MÁS RECIENTES para hacer predicción
    ultimos_datos = datos_limpios[['SMA_20', 'RSI', 'Volatility']].iloc[-1:]

    # Escalar igual que en entrenamiento
    ultimos_datos_scaled = scaler.transform(ultimos_datos)

    # Hacer predicción
    prediccion = modelo.predict(ultimos_datos_scaled)[0]
    probabilidades = modelo.predict_proba(ultimos_datos_scaled)[0]

    # "Preguntarle" al modelo
    decisiones = {0: 'VENDER', 1: 'MANTENER', 2: 'COMPRAR'}
    precio_actual = float(datos_limpios['Close'].iloc[-1])
    print(f"🎯 DECISIÓN DEL MODELO: {decisiones[prediccion]}")
    print(f"📊 CONFIANZA: {probabilidades[prediccion]:.2%}")
    print(f"💰 Precio actual: ${precio_actual:.2f}")

    #Creando Variables derivadas de la prediccion
    decision = decisiones[prediccion]
    confianza = probabilidades[prediccion]
    precio = precio_actual
    return decision, confianza, precio

#Comunicando estados 

    