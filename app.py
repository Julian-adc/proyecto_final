import pandas as pd
import utilidades as util
import streamlit as st
from PIL import Image

#pagina de presentacion o index
st.set_page_config(
    page_title="Analisis del CO2 y el PIB",
    initial_sidebar_state="expanded",
    layout="wide",
    page_icon="🌎"
)

#Lamamos la funcion de archivo utilidad
util.generarMenu()


#Estructura de presentación
left_col, center_col, right_col =st.columns([1,6,1],
                                    vertical_alignment="center")

#edito la columna central 
with center_col:
    st.title("Transición Energética - Analisis del CO2 y el PIB")
    st.write("""
    Relación entre las emisiones de CO₂ y el PIB en Colombia para identificar sectores 
    industriales clave y apoyar la formulación de normativas para reducir sus emisiones.

    En la pagina informes se puede observar los datos y su analisis""")
    
    imagen2 = Image.open("Media\inmagen_principal.png")
    st.image(imagen2, use_container_width=True, width=500,
             caption="Imagen tomada de la web.")