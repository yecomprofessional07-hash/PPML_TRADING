
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
#from .solicitudes import envio
#from .solicitudes import enviar

# modulo_c.py

def procesar_dato(dato, tiempo):
    """Simula el procesamiento del dato."""
    print(f"C: Procesando dato: {dato}")
    dato_procesado = dato
    periodo = tiempo

    # 1. Descargar datos
    empresa = dato_procesado
    datos = yf.download(empresa, period= periodo)

    # --Validar si se descargaron datos
    if datos.empty or len(datos) < 25:
        print(f"Datos insuficientes descargados para {empresa}. Solo hay {len(datos)} registros.")
        return "MANTENER", 0.5, 0

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

    # --Validar datos después de limpiar
    if datos_limpios.empty or len(datos_limpios) < 10:
        print(f"❌ No hay suficientes datos después de limpiar para {empresa}. Solo {len(datos_limpios)} registros válidos.")
        precio_actual = float(datos['Close'].iloc[-1]) if not datos.empty else 0
        return "MANTENER", 0.5, precio_actual

    X = datos_limpios[['SMA_20', 'RSI', 'Volatility']]
    y = datos_limpios['Decision']

    # --Validar características X
    if X.empty or len(X) == 0:
        print(f"❌ No hay características válidas para entrenar el modelo en {empresa}.")
        precio_actual = float(datos_limpios['Close'].iloc[-1])
        return "MANTENER", 0.5, precio_actual

    # 6. Entrenar modelo
    try:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        modelo = LogisticRegression(random_state=42)
        modelo.fit(X_scaled, y)

        print("✅ Modelo entrenado!")

        # Obtener los datos MÁS RECIENTES para hacer predicción
        ultimos_datos = datos_limpios[['SMA_20', 'RSI', 'Volatility']].iloc[-1:]

        # --Validar últimos datos para predicción
        if ultimos_datos.empty:
            print(f"❌ No hay datos recientes para predecir en {empresa}.")
            precio_actual = float(datos_limpios['Close'].iloc[-1])
            return "MANTENER", 0.5, precio_actual

        # Escalar igual que en entrenamiento
        ultimos_datos_scaled = scaler.transform(ultimos_datos)

        # Hacer predicción
        prediccion = modelo.predict(ultimos_datos_scaled)[0]
        probabilidades = modelo.predict_proba(ultimos_datos_scaled)[0]

        # "Preguntarle" al modelo
        decisiones = {0: 'VENDER', 1: 'MANTENER', 2: 'COMPRAR'}
        precio_actual = float(datos_limpios['Close'].iloc[-1])

        #--Usar confianza máxima
        confianza_maxima = np.max(probabilidades)  # La probabilidad más alta entre todas las clases
        confianza_clase_predicha = probabilidades[prediccion]  # Confianza específica de la clase predicha
        
        print(f"🎯 DECISIÓN DEL MODELO: {decisiones[prediccion]}")
        print(f"📊 CONFIANZA: {confianza_maxima:.2%}")
        print(f"🎯 CONFIANZA EN LA DECISIÓN: {confianza_clase_predicha:.2%}")
        print(f"💰 Precio actual: ${precio_actual:.2f}")

        #Creando Variables derivadas de la prediccion
        decision = decisiones[prediccion]
        confianza = confianza_maxima
        precio = precio_actual
        return decision, confianza, precio

    except Exception as e:
        # 🔥 MODIFICACIÓN 5: Manejar errores durante el entrenamiento/predicción
        print(f"❌ Error durante el procesamiento de {empresa}: {str(e)}")
        precio_actual = float(datos['Close'].iloc[-1]) if not datos.empty else 0
        return "MANTENER", 0.5, precio_actual

#Comunicando estados 

    