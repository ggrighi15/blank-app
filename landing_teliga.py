
import streamlit as st

st.set_page_config(page_title="Teliga_bot | Fui Trouxa, Agora Faturei", layout="centered")

st.markdown("# 💔 Fui Trouxa, Agora Faturei")
st.markdown("### Ela sumiu depois do Pix.")
st.markdown("Mas ficou online dois minutos depois...")
st.markdown("O Teliga_bot mostra quem te ignora, manipula ou mente sorrindo.")

st.markdown("——")
if st.button("🔍 Ativar rastreio agora"):
    st.switch_page("teliga_bot_app.py")
else:
    st.markdown("Clique acima para iniciar o rastreio simbólico.")
    
st.markdown("——")
st.markdown("**Powered by Propulsor** | [www.ulsor.com.br](https://www.ulsor.com.br)")
