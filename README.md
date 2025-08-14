# 🚗 Aplicación de Análisis de Datos de Vehículos

Este proyecto es una aplicación web interactiva construida con Streamlit que permite realizar un análisis exploratorio de datos (EDA) sobre un conjunto de datos de venta de vehículos.

## Funcionalidad

La aplicación carga un conjunto de datos desde un archivo `vehicles_us.csv` y ofrece las siguientes visualizaciones interactivas a través de casillas de verificación:

* **Histograma:** Muestra la distribución del kilometraje (odómetro) de los vehículos en el conjunto de datos.
* **Gráfico de Dispersión:** Visualiza la relación entre el kilometraje de un vehículo y su precio de venta.

Esta herramienta permite a los usuarios explorar tendencias y patrones en los datos de manera rápida y visual directamente desde el navegador.

## Cómo Ejecutar
1.  Asegúrate de tener un entorno virtual con `streamlit`, `pandas` y `plotly-express` instalados.
2.  Ejecuta el siguiente comando en la terminal:
    ```bash
    streamlit run app.py
    ```