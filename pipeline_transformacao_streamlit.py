
import pandas as pd
import streamlit as st
from io import BytesIO

def transformar_planilha(df_original):
    novo_cabecalho = df_original.iloc[2]
    df_transformado = df_original[4:].copy()
    df_transformado.columns = novo_cabecalho
    df_transformado.reset_index(drop=True, inplace=True)
    return df_transformado

def main():
    st.title("🚀 Pipeline de Transformação de Planilha Jurídica")

    uploaded_file = st.file_uploader("Faça upload da planilha original", type=["xlsx"])

    if uploaded_file:
        df_original = pd.read_excel(uploaded_file, sheet_name="Smart Report")
        df_transformado = transformar_planilha(df_original)

        st.success("✅ Transformação concluída!")
        st.dataframe(df_transformado.head())

        # Botão para download
        output = BytesIO()
        df_transformado.to_excel(output, index=False)
        st.download_button("📥 Baixar Planilha Transformada", output.getvalue(), file_name="planilha_transformada.xlsx")

if __name__ == "__main__":
    main()
