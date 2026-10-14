import streamlit as st
import json

with open("playlist.json","r", encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

#------------------------------------------ SIDEBAR
st.sidebar.title("Estação Musical")
st.sidebar.image("logo.png")

estilo = st.sidebar.selectbox("Escolha um estilo:", dados['estilo'].keys())
artista = st.sidebar.selectbox("Escolha um artista:", dados['estilo'][estilo]['Artistas'].keys())

#------------------------------------------ BODY

st.title(artista)

video, sobre = st.tabs(["Vídeo","sobre"])

with video:
    st.video(dados['estilo'][estilo]['Artistas'][artista]['música'])

with sobre:

    nome_arquivo = dados['estilo'][estilo]['Artistas'][artista]['sobre']

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()

    st.markdown(texto)

