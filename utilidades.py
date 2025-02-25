import pandas as pd
import streamlit as st 
from PIL import Image
from matplotlib import pyplot as plt 
import seaborn as sns


def generarMenu():
    with st.sidebar:
        col1, col2 = st.columns(2)
        with col1: 
            imagen = Image.open("Media\co2.png")
            st.image(imagen, use_container_width=False, width=80)
        with col2:
            st.header("Analisis del CO2 y el PIB")
            

        st.page_link("app.py", label="Home", icon="🏚️")
        st.page_link("Pages\informe.py", label="infor", icon="📝")

        st.sidebar.title("Menú de Navegación")

        opcion = st.sidebar.radio("Ir a:", ["Emisiones de CO₂ vs. Industria", "Emisiones de CO₂ vs. País vs. Persona", "Emisiones de CO₂ vs. PIB", "Crecimiento Absoluto vs. Porcentual de las Emisiones de CO₂", "Consumo de Energía vs. País vs. Persona", "Participación del País vs. Emisiones Globales de CO₂ vs. Industria", "Cambio de Temperatura Global Atribuido al CO₂ vs. Emisiones Totales del País"])

        if opcion == "Emisiones de CO₂ vs. Industria":
            st.write("")
        elif opcion == "Emisiones de CO₂ vs. País vs. Persona":
            st.write("")        
        elif opcion == "Emisiones de CO₂ vs. PIB":
            st.write("")           
        elif opcion == "Crecimiento Absoluto vs. Porcentual de las Emisiones de CO₂":
            st.write("")    
        elif opcion == "Consumo de Energía vs. País vs. Persona":
            st.write("")   
        elif opcion == "Participación del País vs. Emisiones Globales de CO₂ vs. Industria":
            st.write("") 
        elif opcion == "Cambio de Temperatura Global Atribuido al CO₂ vs. Emisiones Totales del País":
            st.write("")
            
def informedatos(df,titulo):
    df2 = pd.DataFrame(df)
    #Configuramos la visualizacion
    col1, col2, col3 = st.columns([0.5,5,0.5],
                                vertical_alignment="top")
    
    with col1:
        print("")
       
       
    with col2: 
        st.markdown(titulo)
        df2.set_index('Local', inplace=True)
        st.write(df2,unsafe_allow_html=False)
        st.markdown("Grafico de barras")
        
        sns.set_style('whitegrid')
        total = df2.groupby('Local')[['Goles local',
                                     'Goles visitante']].sum()
        goles = pd.DataFrame(total)
        goles['Goles Total'] = goles['Goles local'] + goles['Goles visitante']
        goles = goles.reset_index()

        resultado = goles.groupby(['Local']).sum()
        resultado.plot(kind='bar', figsize=(10,10))
        plt.tight_layout()
        st.pyplot(plt)

    resultado = goles.groupby(['Local']).sum()
    resultado.plot(kind='bar', figsize=(10,10))
    plt.tight_layout()
    st.pyplot(plt)

    sns.set_style('whitegrid')
    #Agrupamos por equipos para que muestre la suma de los goles locales
    resultado = df.groupby('Local')['Goles local'].sum()
    resultado.plot(kind='pie', autopct='%1.2f%%',
                figsize=(15,15), ylabel='',
                fontsize=15)
    plt.title('Porcentaje de goles marcados por equipo local').set_fontsize(20)
    plt.show()