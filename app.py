# 1. Importar las librerías
import streamlit as st
import pandas as pd
import plotly.express as px

# 2. Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv') 

# 3. Crear un encabezado
st.header('Cuadro de Mandos de Datos de Vehículos')

# 4. Crear una casilla de verificación para el histograma
if st.checkbox('Construir histograma de odómetro'):
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar la gráfica
    st.plotly_chart(fig, use_container_width=True)

# 5. Crear una casilla de verificación para el gráfico de dispersión
if st.checkbox('Construir gráfico de dispersión'):
    st.write('Creación de un gráfico de dispersión para comparar odómetro vs. precio')

    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")

    # Mostrar la gráfica
    st.plotly_chart(fig_scatter, use_container_width=True)