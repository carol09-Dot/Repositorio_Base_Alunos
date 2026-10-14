import streamlit as st
import requests
import json

st.set_page_config(layout="wide")

with open ("pokemon_index.json", "r", encoding="utf-8") as arquivo:
    id_pokemons = json.load(arquivo)

with open("raridade.json", "r", encoding="utf-8") as arquivo:
    raridade = json.load(arquivo)

classific = st.sidebar.selectbox("Classsificação", raridade.keys())
nome_pokemon = st.sidebar.selectbox("Pokémon", raridade[classific])

st.title("Pokedex")
#nome_pokemon = st.selectbox("escolha o pokemón:", id_pokemons.values())


dados_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}").json()
st.title(dados_pokemon['name'].title())

col1, col2, col3 = st.columns(3)

with col1:
    st.image(dados_pokemon['sprites']['front_default'], width=300)

with col2:
    st.audio(dados_pokemon['cries']['latest'])
    st.subheader("Tipos:")
    for tipo in dados_pokemon ['types']:
        st.markdown(f"- {tipo['type']['name']}")

with col3:
    st.image(dados_pokemon['sprites']['front_shiny'], width=300)

st.markdown("---")

col1, col2, col3 = st.columns(3)

altura = dados_pokemon['height']/10

peso = dados_pokemon['weight']/10

imc = round(peso / (altura* altura), 2)

with col1:
    st.metric("Altura",altura)

with col2:
    st.metric("IMC",imc)

with col3:
    st.metric("Peso", peso)


ataques, status, locais, habilidades = st.tabs(["Ataques","Status","Locais","Habilidades"])

with ataques:
    st.subheader(f"Quantidades de ataques(movimentos): {len(dados_pokemon['moves'])}")
    for move in dados_pokemon['moves']:
        st.markdown(f"- {move['move']['name']}")

with status:
    hp = dados_pokemon['stats'][0]['base_stat']
    ataque = dados_pokemon['stats'][1]['base_stat']
    defesa = dados_pokemon['stats'][2]['base_stat']
    ataque_especial = dados_pokemon['stats'][3]['base_stat']
    defesa_especial = dados_pokemon['stats'][4]['base_stat']
    velocidade = dados_pokemon['stats'][5]['base_stat']

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.metric("HP",hp)

    with col2:
        st.metric("Ataques",ataque)

    with col3:
        st.metric("Defesa",defesa)

    with col4:
        st.metric("Ataque especial",ataque_especial)

    with col5:
        st.metric("Defesa especial",defesa_especial)

    with col6:
        st.metric("Velocidade",velocidade)

    with locais:
        rota_locais = dados_pokemon['location_area_encounters']
        dados_locais = requests.get(rota_locais).json()
        for local in dados_locais:
            st.markdown(f"- {local["location_area"]["name"]}")

with habilidades:
    for hab in dados_pokemon['abilities']:
        st.markdown(f"- {hab['ability']['name']}")