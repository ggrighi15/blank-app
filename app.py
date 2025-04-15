import pandas as pd
import json
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

# Função para carregar e validar dados JSON
def carregar_e_validar_dados():
    with open('db_risco.json', encoding='utf-8') as f:
        db_risco = json.load(f)

    with open('db_categoria.json', encoding='utf-8') as f:
        db_categoria = json.load(f)

    with open('db_polo.json', encoding='utf-8') as f:
        db_polo = json.load(f)

    with open('db_depositos.json', encoding='utf-8') as f:
        depositos = json.load(f)

    df_depositos = pd.json_normalize(depositos)

    data_cols = ["Data_Encerramento", "Iniciado_em", "Resgatado_em"]
    for col in data_cols:
        df_depositos[col] = pd.to_datetime(df_depositos[col], errors='coerce').dt.strftime('%d/%m/%Y')

    df_depositos['Total_depositado'] = pd.to_numeric(df_depositos['Total_depositado'].astype(str).str.replace(',', '.', regex=False), errors='coerce')
    df_depositos['Total_resgatado'] = pd.to_numeric(df_depositos['Total_resgatado'], errors='coerce').fillna(0)

    df_depositos = df_depositos.dropna(subset=["Cliente", "Banco", "Número", "Total_depositado"])
    df_depositos = df_depositos[df_depositos['Total_resgatado'] <= df_depositos['Total_depositado']]
    df_depositos['Encerrado'] = df_depositos['Data_Encerramento'].apply(lambda x: 'Sim' if pd.notnull(x) else 'Não')

    return df_depositos

@app.route('/dados_validados', methods=['GET'])
def obter_dados_validados():
    formato = request.args.get('formato', 'json').lower()
    df = carregar_e_validar_dados()

    if formato == 'excel':
        filename = 'depositos_validados.xlsx'
        df.to_excel(filename, index=False)
        return send_file(filename, as_attachment=True)

    elif formato == 'csv':
        filename = 'depositos_validados.csv'
        df.to_csv(filename, index=False)
        return send_file(filename, as_attachment=True)

    elif formato == 'json':
        return jsonify(df.to_dict(orient='records'))

    return jsonify({"erro": "Formato não suportado"}), 400

# Endpoint Dashboard em JSON
@app.route('/dashboard', methods=['GET'])
def dashboard():
    df = carregar_e_validar_dados()
    return jsonify(df.to_dict(orient='records'))

# Endpoint para comparar dados entre Fevereiro e Março de 2025
@app.route('/comparar', methods=['GET'])
def comparar_periodos():
    df_fev = pd.read_excel('02-2025.xlsx')
    df_marco = pd.read_excel('03-2025.xlsx')

    comparacao = pd.merge(df, df_marco, on='Cliente', suffixes=('_02_2025', '_03_2025'))
    comparacao['Diferenca'] = comparacao['Total_depositado_03_2025'] - comparacao['Total_depositado_02_2025']

    return jsonify(comparacao.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)
