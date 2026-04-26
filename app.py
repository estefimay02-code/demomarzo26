import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title('Mi Primera Aplicación Streamlit con Datos y Gráficas')

st.header('DataFrame de Ejemplo')

# Crear un DataFrame de ejemplo
data = {
    'Fecha': pd.to_datetime(pd.date_range(start='2023-01-01', periods=10)),
    'Ventas': np.random.randint(100, 500, size=10),
    'Gastos': np.random.randint(50, 200, size=10),
    'Beneficio': np.random.randint(10, 300, size=10)
}
df = pd.DataFrame(data)

# Mostrar el DataFrame
st.dataframe(df)

st.header('Gráfica de Línea de Ventas y Gastos')

# Establecer 'Fecha' como índice para la gráfica de línea
df_plot = df.set_index('Fecha')

# Crear una gráfica de línea para 'Ventas' y 'Gastos'
st.line_chart(df_plot[['Ventas', 'Gastos']])

st.write("\nEsta es una aplicación simple de Streamlit que demuestra cómo mostrar datos tabulares y visualizarlos con una gráfica de línea.")
