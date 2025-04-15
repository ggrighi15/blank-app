
import pandas as pd
import numpy as np
import streamlit as st

def gerar_tabela_dinamica(df_comparativo, db_clientes, db_categoria, db_risco, db_polo):
    df_final = df_comparativo.copy()

    # 1. Clientes: Cliente (FR_2025) → Clientes (db_clientes)
    df_final = df_final.merge(db_clientes[['Clientes', '#Clientes']], left_on="Cliente", right_on="Clientes", how="left")

    # 2. Categoria: Categoria (FR_2025) → Categoria (db_categoria)
    df_final = df_final.merge(db_categoria[['Categoria', '#Categoria']], on="Categoria", how="left")

    # 3. Risco Atual: normalizar para A/B/C
    df_final['#Risco'] = np.where(df_final['Risco Atual'].str.contains("Provável", na=False), "A - Provável",
                           np.where(df_final['Risco Atual'].str.contains("Possível", na=False), "B - Possível",
                           np.where(df_final['Risco Atual'].str.contains("Remota", na=False), "C - Remota", None)))

    # 4. Polo: Situação (FR_2025) → Polo (db_polo)
    df_final = df_final.merge(db_polo[['Polo']], left_on="Situação", right_on="Polo", how="left")

    # Limpar e organizar os dados finais para a pivot table
    valor_coluna = "Valor analisado" if "Valor analisado" in df_final.columns else df_final.columns[-1]
    df_final[valor_coluna] = pd.to_numeric(df_final[valor_coluna], errors='coerce').fillna(0)

    # Tabela dinâmica ajustada com relacionamentos corrigidos
    pivot_ajustada = pd.pivot_table(
        df_final,
        index=["#Categoria", "Polo", "#Clientes"],
        columns="#Risco",
        values=valor_coluna,
        aggfunc="sum",
        fill_value=0
    )

    return pivot_ajustada

# Interface Streamlit
st.title("Painel de Análise Jurídica - Tabela Dinâmica")

# Upload dos arquivos necessários
st.sidebar.header("📂 Upload dos Arquivos")
df_file = st.sidebar.file_uploader("Arquivo base (df_comparativo)", type=["xlsx"])
clientes_file = st.sidebar.file_uploader("db_clientes.json", type=["json"])
categoria_file = st.sidebar.file_uploader("db_categoria.json", type=["json"])
risco_file = st.sidebar.file_uploader("db_risco.json", type=["json"])
polo_file = st.sidebar.file_uploader("db_polo.json", type=["json"])

if all([df_file, clientes_file, categoria_file, risco_file, polo_file]):
    df_comparativo = pd.read_excel(df_file)
    db_clientes = pd.read_json(clientes_file)
    db_categoria = pd.read_json(categoria_file)
    db_risco = pd.read_json(risco_file)
    db_polo = pd.read_json(polo_file)

    tabela_resultado = gerar_tabela_dinamica(df_comparativo, db_clientes, db_categoria, db_risco, db_polo)
    st.success("✅ Tabela dinâmica gerada com sucesso!")
    st.dataframe(tabela_resultado)
else:
    st.warning("⚠️ Faça o upload de todos os arquivos para gerar a tabela.")
