import streamlit as st
import json
import time
from datetime import datetime
st.set_page_config(layout='wide', page_icon="💬")

# --- Funções auxiliares ---
def carregar_mensagens():
    with open('mensagens.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_mensagens(mensagens):
    with open('mensagens.json', 'w', encoding='utf-8') as f:
        json.dump(mensagens, f, indent=4, ensure_ascii=False)

# --- Sidebar ---
username = st.sidebar.text_input('Nome de usuário', key="username", value="guest")
prompt = st.chat_input("Digite uma mensagem")

# --- Se o usuário enviou algo ---
if prompt:
    mensagens = carregar_mensagens()
    t = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    mensagens.insert(0,{"time": f'({t})', "username": username, "mensagem": prompt})
    salvar_mensagens(mensagens)
    st.rerun()  # recarrega a página após enviar mensagem

# --- Título ---
st.title("💬 Chat entre usuários")

# --- Container para mensagens ---
chat_container = st.empty()

# --- Loop de atualização automática ---
# OBS: isso roda por um tempo finito, não infinito, pra não travar o app
for _ in range(1000):  # atualiza ~1000 vezes (você pode ajustar)
    mensagens = carregar_mensagens()

    with chat_container.container(border=True, height=500):
        for msg in mensagens:
            st.write(f"**{msg['time']} - {msg['username']}**: {msg['mensagem']}")

    time.sleep(5)  # intervalo de atualização (3 segundos)
    st.rerun()  # força atualização
