import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.header("Este es un encabezado interactivo")

hist_button = st.button('Crear histograma') #crear un botón
     
if hist_button:#al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(df, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Crear dispersion')

if disp_button:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(df, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)




