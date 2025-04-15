import os
import pandas as pd
import hashlib
from datetime import datetime, timedelta
import streamlit as st

# Configurações
RAIZ = 'C:\\'
extensoes = ('.xlsx', '.xls', '.csv')
hoje = datetime.now()
limite_data = hoje - timedelta(days=730)

st.title("🧹 Detector de Planilhas Obsoletas")

# Botão para iniciar
if st.button(r"🔍 Iniciar varredura em C:\"):
    mantidos = []
    excluidos = []
    hashes = set()

    progresso = st.progress(0)
    arquivos_listados = []

    for dirpath, _, files in os.walk(RAIZ):
        for nome_arquivo in files:
            if nome_arquivo.lower().endswith(extensoes):
                arquivos_listados.append(os.path.join(dirpath, nome_arquivo))

    total = len(arquivos_listados)

    for idx, caminho in enumerate(arquivos_listados):
        progresso.progress((idx + 1) / total)
        nome_arquivo = os.path.basename(caminho)
        try:
            modificado = datetime.fromtimestamp(os.path.getmtime(caminho))

            if nome_arquivo.lower().endswith('.csv'):
                df = pd.read_csv(caminho, encoding='utf-8', sep=None, engine='python')
            else:
                df = pd.read_excel(caminho, engine='openpyxl')

            vazio = df.empty
            hash_df = hashlib.md5(pd.util.hash_pandas_object(df, index=True).values).hexdigest()
            duplicado = hash_df in hashes
            if not duplicado:
                hashes.add(hash_df)

            nome_suspeito = any(x in nome_arquivo.lower() for x in ['cópia', 'old', 'backup'])
            muito_antigo = modificado < limite_data

            if vazio or duplicado or nome_suspeito or muito_antigo:
                excluidos.append([nome_arquivo, caminho, modificado, 'vazio' if vazio else '', 'duplicado' if duplicado else '', 'nome suspeito' if nome_suspeito else '', 'antigo' if muito_antigo else ''])
            else:
                mantidos.append([nome_arquivo, caminho, modificado])

        except Exception as e:
            excluidos.append([nome_arquivo, caminho, 'erro', 'erro ao abrir'])

    df_mantidos = pd.DataFrame(mantidos, columns=['Arquivo', 'Caminho', 'Última Modificação'])
    df_excluidos = pd.DataFrame(excluidos, columns=['Arquivo', 'Caminho', 'Última Modificação', 'Vazio', 'Duplicado', 'Nome Suspeito', 'Antigo'])

    st.subheader("✅ Planilhas que devem ser mantidas")
    st.dataframe(df_mantidos)

    st.subheader("🗑️ Planilhas candidatas à exclusão")
    st.dataframe(df_excluidos)

    st.download_button("📥 Baixar planilhas mantidas", data=df_mantidos.to_csv(index=False).encode(), file_name="planilhas_mantidas.csv")
    st.download_button("📥 Baixar planilhas para exclusão", data=df_excluidos.to_csv(index=False).encode(), file_name="planilhas_para_exclusao.csv")