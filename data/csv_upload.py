import streamlit as st
import pandas as pd

def main():
    st.title("Subir Archivo CSV con Streamlit")

    # Crear un widget para cargar el archivo CSV
    uploaded_file = st.file_uploader("Elige un archivo CSV", type=["csv"])

    if uploaded_file is not None:
        # Leer el archivo CSV en un DataFrame de Pandas
        df = pd.read_csv(uploaded_file)

        # Mostrar el DataFrame
        st.write("Contenido del archivo CSV:")
        st.write(df)

        # Aquí puedes realizar operaciones adicionales con el DataFrame si es necesario

if __name__ == "__main__":
    main()
