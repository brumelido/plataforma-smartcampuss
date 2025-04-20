import streamlit as st
import os

st.set_page_config(page_title="Painel SmartCampus", layout="centered")
st.title("📡 Painel de Monitoramento - SmartCampus")

CAMINHO_ARQUIVO = "dados_sensor.txt"

if os.path.exists(CAMINHO_ARQUIVO):
    with open(CAMINHO_ARQUIVO, "r") as f:
        linhas = f.readlines()
        if linhas:
            dado = linhas[-1].strip()
            tipo, valor = map(str.strip, dado.split(":"))
            st.metric(label=f"Sensor: {tipo}", value=f"{valor}")
        else:
            st.warning("Nenhum dado disponível.")
else:
    st.error("Arquivo de dados não encontrado.")
