# Proyecto de Srpint 7
Mi proyecto sprint 7 de aplicación dentro de Tripleten
Este proyecto utiliza Python, Aplicación interactiva desarrollada con **Streamlit** y **Plotly Express** para explorar un conjunto de datos de anuncios de venta de coches en Estados Unidos.

La app permite:
- Visualizar histogramas y diagramas de dispersión.
- Aplicar filtros interactivos mediante casillas de verificación (*checkboxes*).
- Explorar relaciones entre kilometraje (`odometer`), precio (`price`), tipo de vehículo (`type`) y otras variables.

## Requisitos
- Python 3.10 o superior
- Streamlit
- Plotly-express

## Instalación
pip install -r requirements.txt

## Uso
streamlit run app.py


## Estructura del proyecto
├── README.md           # Información del proyecto
├── app.py              # Código principal de la app en Streamlit
├── vehicles_us.csv     # Insumos utilizados para el proyecto
├── requirements.txt    # Librerías necesarias
└── notebooks           # Datos de entrada
    └── EDA.ipynb

## Creditos
Jorge Arturo Reyna Rosas - Data Analyst Tripleten
Ricardo Huilipan - Coach Tripleten
