import streamlit as st
import pandas as pd 
import plotly.express as px
import time

# Encabezado con emoji
st.title('Visualizaciones de datos para el conjunto de datos de anuncio de venta de coches 📊')

car_data = pd.read_csv("vehicles_us.csv") # leer los datos

# Añadir espacio entre el título y las casillas de verificación
st.write('')

# Añadir casillas de verificación para histograma y diagrama de dispersión
show_histogram = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar diagrama de dispersión')

# Agregar botón "Mostrar" con efectos hover y luz
button = st.button('Mostrar', help='Haz clic para mostrar las visualizaciones')

# Validar si se han seleccionado casillas antes de mostrar las visualizaciones
if button:
    if not show_histogram and not show_scatter: # Si ninguna casilla está seleccionada
        # Mostrar mensaje de advertencia
        st.warning('Por favor, selecciona alguna casilla antes de continuar ✅')
    else:
        # Mostrar spinner de carga
        with st.spinner('Cargando datos... por favor, espera. 😊'):
            # Esperar 2 segundos
            time.sleep(2)

            # Mostrar los diagramas después de 2 segundos
            if show_histogram: # Si la casilla de verificación del histograma está seleccionada
                # Escribir un mensaje en pantalla
                st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
                
                # Crear el histograma
                hist = px.histogram(car_data, x='odometer')
                
                # Mostrar el histograma
                st.plotly_chart(hist, use_container_width=True) 
        
            if show_scatter: # Si la casilla de verificación del diagrama de dispersión está seleccionada
                # Escribir un mensaje en pantalla
                st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
                
                # Crear el diagrama de dispersión
                scatter = px.scatter(car_data, x='odometer', y='price')
                
                # Mostrar el diagrama de dispersión
                st.plotly_chart(scatter, use_container_width=True)





    
    

    