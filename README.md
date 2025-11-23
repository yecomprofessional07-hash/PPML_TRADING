# PPML_TRADING | PROYECTO DE PROGRAMACIÓN II

Integrantes:

    - fablizan

    - LoximtoMedina

    - yecomprofessional07-hash

    - sheylyy
    
Este proyecto es una plataforma interactiva de simulación bursátil, desarrollada íntegramente en Streamlit, Pandas y Sklearn, que permite a los usuarios explorar, analizar y gestionar acciones de distintas empresas mediante datos obtenidos desde una API financiera y respaldados localmente en archivos CSV, así como implementación de modelos de regresion logística.

El sistema simula un entorno de inversión donde cada usuario puede iniciar sesión, manejar su presupuesto, comprar o vender acciones, y visualizar métricas relevantes para las acciones a tomar por el usuario.

Guía de instalación
    1. Clone el Repositorio github
    2. Haga pip install -r requirements.txt
    3. Haga python -m streamlit run app.py

Decisiones de Diseño:
    1. Modelo Full-Stack Integrado: 
        1.1 Aplicacion Monolitica: Frontend y backend implementados en el mismo proyecto
        1.2 Datos importados: Yahoo finance proporciona datos historicos
        1.3 Streamlit Framework: Aplicación multipágina con recargas completas
        1.4 Modelo ML: uso de LogisticRegression con sklearn, pandas y numpy
    2. Estructura:
        PPML_TRADING
        |__Data
        |    |__users.csv
        |__model
        |    |__ __init__.py
        |    |__BuscarAcciones.py
        |    |__solicitudes.py
        |__pages
        |    |__ __init__.py
        |    |__aboutUs.py
        |    |__principal.py
        |    |__settings.py
        |    |__signUp.py
        |__sources
        |    |__profileImage1.png
        |    |__profileImage2.png
        |    |__profileImage3.png
        |__app.py
        |__requirements
        |__requirements.txt
        |__ __init__.py
        |__README.md
        |__.streamlit
        |    |__config.toml
        |__env
        
Prueba de Despliegue
    url: https://ppml-trading.onrender.com
    

Ultima actualización realizada el 23 de noviembre del 2025 a las 13pm
