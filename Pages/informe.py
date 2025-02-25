import pandas as pd
import utilidades as util
import streamlit as st
from matplotlib import pyplot
import seaborn as sns

#Configuramos encabezado de pagina
st.set_page_config(
    page_title="Analisis del CO2 y el PIB",
    initial_sidebar_state="expanded",
    layout="centered",
    page_icon="🌎"
)

util.generarMenu()


#Visualización
st.title("Evolución Global del CO₂ y el PIB (2000-2023): Análisis y Relevancia para las Políticas Públicas en Colombia")
ruta = "Data/tctClean.csv"
df = pd.read_csv(ruta)
tex = "Este estudio presenta un análisis de los datos relevantes sobre la generación de CO₂ y el PIB a nivel mundial desde el año 2000 hasta 2023. Se examina la correlación y variabilidad de estos indicadores en el contexto de su evolución global. El objetivo es comprender estos cambios para orientar el diseño y evaluación de políticas públicas en Colombia, con un enfoque en los distintos sectores industriales."
util.informedatos(df, tex)

