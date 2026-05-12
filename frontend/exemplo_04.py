# poetry add streamlit pandas

import streamlit as st
import pandas as pd
import subprocess

# Função para carregar os dados do arquivo CSV
def load_data():
    df = pd.read_csv("execution_logs.log")
    return df


# Função para executar o script Python
def run_python_script():
    subprocess.run(["poetry", "run", "python", "pipeline/pipeline.py"])

# Layout do aplicativo Streamlit
def main():
    st.title("Visualização de Logs e Execução de Scripts")
    st.image("pics/AirflowLogo.png")

    # Carregar os dados do arquivo CSV
    df = load_data()

    #Exibir os dados na interface do streamlit
    st.write("Logs de execução:", df)

    #botão para atualizar os dados
    if st.button("Atualizar dados"):
        df = load_data()
        st.write("Dados atualizados com sucesso!")

    #botão para executar script python
    if st.button("Executar script python"):
        run_python_script()
        st.write("Script python executado com sucesso!")

if __name__ == "__main__":
    main()