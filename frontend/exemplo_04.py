# poetry add streamlit pandas

import streamlit as st
import pandas as pd
import subprocess

# Função para carregar os dados do arquivo CSV
def load_data():
    try:
        df = pd.read_csv("execution_logs.log", header=None, names=["Logs"])
        return df
    except Exception:
        return pd.DataFrame(columns=["Logs"])


# Função para executar o script Python
def run_python_script():
    subprocess.run(["poetry", "run", "python", "pipeline/pipeline.py"])

# Layout do aplicativo Streamlit
def main():
    st.title("Visualização de Logs e Execução de Scripts")
    st.image("pics/AirflowLogo.png")


     # Carregar e exibir os dados SEMPRE no final para mostrar o estado atual
    df = load_data()
    st.write("Logs de execução:")
    st.dataframe(df, use_container_width=True)

    # botões para ações
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Atualizar dados"):
            st.write("Dados atualizados!")

    with col2:
        if st.button("Executar script python"):
            with st.spinner("Executando pipeline..."):
                run_python_script()
                st.success("Script python executado com sucesso!")

   

if __name__ == "__main__":
    main()