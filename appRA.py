import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # Configurar la página para que ocupe todo el ancho
    st.set_page_config(layout="wide")

    # Título centrado
    st.title("EDA de Planta")

    # Nombre del archivo predeterminado
    default_file_name = "Data_Mayor_Train_CSV.csv"

    # Leer el archivo CSV predeterminado
    if os.path.exists(default_file_name):
        df_MG = pd.read_csv(default_file_name, encoding='latin-1')  # Cambia 'latin-1' según sea necesario
    else:
        st.error("El archivo predeterminado no se encuentra en la carpeta del proyecto.")
        return

    # Mostrar estadísticas descriptivas como tabla
    st.write("Estadísticas Descriptivas del Dataset:")
    st.dataframe(df_MG.describe())

    # Graficar interpretación para reemplazo de valores de Malla -200
    st.subheader("Interpretación para reemplazo de valores de Malla -200")
    plt.figure(figsize=(10, 3))

    # Subgráfico 1: Malla -200 original
    plt.subplot(1, 3, 1)
    df_MG['% Malla -200'].hist()
    plt.title('%Malla -200 (Original)')

    # Subgráfico 2: Malla -200 con media
    plt.subplot(1, 3, 2)
    df_MG['% Malla -200'].fillna(df_MG['% Malla -200'].mean()).hist()
    plt.title('%Malla -200 (Media)')

    # Subgráfico 3: Malla -200 con mediana
    plt.subplot(1, 3, 3)
    df_MG['% Malla -200'].fillna(df_MG['% Malla -200'].median()).hist()
    plt.title('%Malla -200 (Mediana)')

    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)

    # Graficar interpretación para reemplazo de valores de Horas de Operación
    st.subheader("Interpretación para reemplazo de valores de Horas de Operación")
    plt.figure(figsize=(10, 3))

    # Subgráfico 1: Horas de Operación original
    plt.subplot(1, 3, 1)
    df_MG['Hrs Operacion'].hist()
    plt.title('Hrs Operacion (Original)')

    # Subgráfico 2: Horas de Operación con media
    plt.subplot(1, 3, 2)
    df_MG['Hrs Operacion'].fillna(df_MG['Hrs Operacion'].mean()).hist()
    plt.title('Hrs Operacion (Media)')

    # Subgráfico 3: Horas de Operación con mediana
    plt.subplot(1, 3, 3)
    df_MG['Hrs Operacion'].fillna(df_MG['Hrs Operacion'].median()).hist()
    plt.title('Hrs Operacion (Mediana)')

    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)

if __name__ == "__main__":
    main()




