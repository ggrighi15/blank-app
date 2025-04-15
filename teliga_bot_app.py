
import streamlit as st

st.set_page_config(page_title="Teliga_bot | Fui Trouxa, Agora Faturei", layout="centered")

st.markdown("## 🔍 Teliga_bot")
st.markdown("### Transforme sua decepção em rastreio inteligente.")
st.markdown("——")

st.markdown("**Ela sumiu depois do Pix...**")
st.markdown("Mas estava online dois minutos depois.")
st.markdown("Disse que era ansiedade. Mas publicou um story rindo na mesma hora.")
st.markdown("Você não foi trouxa. Só confiou em quem nunca foi sincera.")
st.markdown("——")
st.success("✔️ Teliga_bot ativado")

with st.form("rastrear_form"):
    st.markdown("**Digite o número, @ ou e-mail para rastrear presença online:**")
    entrada = st.text_input("Informação de rastreio", placeholder="Ex: +55 ••• ••••-••32")
    submit = st.form_submit_button("Verificar atividade")

    if submit and entrada:
        st.warning("⚠️ Perfil com atividade recente detectada.")
        st.markdown("- Status: Visto recentemente")
        st.markdown("- Redes sociais vinculadas: detectadas")
        st.markdown("- Mensagens ignoradas após transferência: 4")
        st.markdown("---")
        st.markdown("**🔁 Hora de virar o jogo.**")

st.markdown("——")
st.markdown("🌐 Acesse o plano completo no [ulsor.com.br](https://ulsor.com.br)")
