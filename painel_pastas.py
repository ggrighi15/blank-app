{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "b7fbd50d",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mFalha ao iniciar o Kernel. \n",
      "\u001b[1;31mSyntaxError: invalid syntax. \n",
      "\u001b[1;31mConsulte o <a href='command:jupyter.viewOutput'>log</a> do Jupyter para obter mais detalhes."
     ]
    }
   ],
   "source": [
    "# painel_pastas.py\n",
    "import streamlit as st\n",
    "import os\n",
    "\n",
    "# Dicionário com mapeamento dos módulos\n",
    "pastas_info = {\n",
    "    \"Contencioso\": {\n",
    "        \"caminho\": \"C:/data_base/Contencioso\",\n",
    "        \"descrição\": \"Base de dados processual e auditorias do contencioso.\",\n",
    "        \"ações\": [\"Consolidar DB\", \"Validar dados críticos\", \"Conectar ao BI\"]\n",
    "    },\n",
    "    \"Contratos\": {\n",
    "        \"caminho\": \"C:/data_base/Contratos\",\n",
    "        \"descrição\": \"Repositório de contratos e cláusulas contratuais.\",\n",
    "        \"ações\": [\"Gerar alertas\", \"Organizar vencimentos\", \"Extrair partes\"]\n",
    "    },\n",
    "    \"data_base\": {\n",
    "        \"caminho\": \"C:/data_base/data_base\",\n",
    "        \"descrição\": \"Pasta genérica (possível lixo ou estrutura redundante).\",\n",
    "        \"ações\": [\"Revisar conteúdo\", \"Unificar ou excluir\"]\n",
    "    },\n",
    "    \"DJE\": {\n",
    "        \"caminho\": \"C:/data_base/DJE\",\n",
    "        \"descrição\": \"Captura de publicações no Diário da Justiça Eletrônico.\",\n",
    "        \"ações\": [\"Organizar por tribunal\", \"Validar nomes\", \"Gerar alertas\"]\n",
    "    },\n",
    "    \"flask_session\": {\n",
    "        \"caminho\": \"C:/data_base/flask_session\",\n",
    "        \"descrição\": \"Sessões temporárias do backend Flask.\",\n",
    "        \"ações\": [\"Proteger com token\", \"Limpar sessões antigas\"]\n",
    "    },\n",
    "    \"flask-uvicorn-app\": {\n",
    "        \"caminho\": \"C:/data_base/flask-uvicorn-app\",\n",
    "        \"descrição\": \"API principal em Flask ou FastAPI.\",\n",
    "        \"ações\": [\"Rodar Uvicorn\", \"Proteger rotas\", \"Testar integração\"]\n",
    "    }\n",
    "}\n",
    "\n",
    "st.set_page_config(page_title=\"Painel das Pastas\", layout=\"wide\")\n",
    "st.title(\"📂 Painel de Desenvolvimento de Pastas\")\n",
    "st.caption(\"Monitoramento direto da estrutura `C:/data_base`\")\n",
    "\n",
    "for nome, info in pastas_info.items():\n",
    "    with st.expander(f\"📁 {nome}\"):\n",
    "        st.markdown(f\"**Descrição**: {info['descrição']}\")\n",
    "        st.markdown(f\"**Caminho**: `{info['caminho']}`\")\n",
    "\n",
    "        st.markdown(\"**Ações recomendadas**:\")\n",
    "        for acao in info[\"ações\"]:\n",
    "            st.checkbox(f\"{acao}\", key=f\"{nome}_{acao}\")\n",
    "        \n",
    "        if not os.path.exists(info['caminho']):\n",
    "            st.warning(\"⚠️ Pasta não encontrada. Verifique o caminho.\")\n",
    "        else:\n",
    "            st.success(\"✅ Pasta encontrada no sistema.\")\n",
    "\n",
    "st.sidebar.success(\"Use a barra lateral para expandir módulos.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
