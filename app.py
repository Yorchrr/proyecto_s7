import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.header("Proyecto sprint 7 — Visualizaciones con casillas de verificación")

st.write("Marca las casillas para mostrar las visualizaciones. Opcionalmente, aplica filtros sencillos.")

filtro_4wd = st.checkbox("Mostrar solo vehículos 4WD (is_4wd == 1)")
quitar_nulos = st.checkbox("Quitar filas con valores NaN en las columnas usadas")
hist_button = st.button('Crear histograma') #Boton de histograma

df_viz = df.copy()
if filtro_4wd:
    df_viz = df_viz[pd.to_numeric(df_viz["is_4wd"], errors="coerce") == 1]

ver_hist = st.checkbox("Mostrar histograma de odómetro")

if ver_hist:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    datos_hist = df_viz[["odometer"]].copy()
    if quitar_nulos:
        datos_hist = datos_hist.dropna(subset=["odometer"])

    fig_hist = px.histogram(
        datos_hist,
        x="odometer",
        nbins=30,
        title="Distribución de odómetro"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

ver_disp = st.checkbox("Mostrar diagrama de dispersión (odómetro vs precio)")
log_precio = st.checkbox("Usar escala logarítmica en el precio (y)")

if ver_disp:
    st.write("Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches")

    cols = ["odometer", "price"]
    datos_disp = df_viz[cols].copy()

    if quitar_nulos:
        datos_disp = datos_disp.dropna(subset=cols)
    
    fig_disp = px.scatter(
        datos_disp,
        x="odometer",
        y="price",
        title="Relación entre odómetro y precio",
        labels={"odometer": "Kilometraje (odometer)", "price": "Precio (price)"},
        opacity=0.6,
        log_y=log_precio
    )
    st.plotly_chart(fig_disp, use_container_width=True)

         
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




