#================================= Importaciones/Librerías ================================#
import streamlit as st

#=============================== Configuración de la página ===============================#
st.set_page_config(page_title="Gestor de Trading Basado en ML", layout="centered")

#====================================== Contenido principal ======================================#
# Primera fila: Título
st.markdown("""
<h1 style='text-align: center;'>GESTOR DE TRADING BASADO EN ML</h1>
            
---
            
### Acerca de Nosotros
Bienvenido a nuestro Gestor de Trading Basado en Machine Learning. Esta aplicación ha sido desarrollada para ayudar a los usuarios a tomar decisiones informadas sobre sus inversiones en el mercado de valores utilizando técnicas avanzadas de aprendizaje automático.

---

**Nuestro Equipo:**
- **Desarrollador backend:** Erin Yareth Soza Euceda
- **Diseñador de UX/UI:** Cristian Josué Medina Galeano
- **Programadores frontend:** Ashley Fabiola mimi mimimimi, Cristian Josué Medina Galeano, Sheyly nosé nosé nosé
- **Documentación y pruebas:** Erin Yareth Soza Euceda, Neyzer nosé nosé nosé

---
            
**Objetivo del Proyecto:**
Nuestro objetivo es proporcionar una herramienta intuitiva y eficaz que permita a los usuarios gestionar sus carteras de inversión con la ayuda de algoritmos de machine learning, facilitando así la toma de decisiones en un entorno financiero dinámico.

---

**Contacto:**
Si tienes alguna pregunta o deseas obtener más información sobre nuestro proyecto, no dudes en contactarnos en CorreoFicticio@gmail.com.

---""", unsafe_allow_html=True)

# Botón para volver a principal.py
if st.button("Volver", use_container_width=True):
    st.switch_page("pages/principal.py")