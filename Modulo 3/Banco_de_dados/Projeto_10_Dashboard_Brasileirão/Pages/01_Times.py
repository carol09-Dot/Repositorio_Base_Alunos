import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Análise dos Times",
    page_icon="⚽",
    layout='wide'
)

st.title("⚽ Análise dos Times de Futebol")
st.markdown('Explore os dados dos clubes, compare as vitórias e acompanhe a evolução do valor dos times ao longo dos anos.')
st.divider()

df = pd.read_csv("Tabela_Clubes.csv")

lista_anos = df['Ano'].unique().tolist()

filtro_anos = st.sidebar.multiselect('Selecione o ano', lista_anos, default=lista_anos)
df = df[df['Ano'].isin(filtro_anos)]


st.subheader("Dados dos times")
st.dataframe(df.head())
st.subheader("Resumo dos dados")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Quantidade de registros", len(df))

with col2:
    st.metric("Quantidade de clubes", df['Clubes'].nunique())

with col3:
    media_vitorias = df['Vitorias'].mean()
    st.metric('Média de vitórias', f'{media_vitorias:.1f}')

st.subheader('Vitórias por clube')
grafico = px.bar(
    df,
    x='Clubes',
    y='Vitorias',
    color="Ano",
    title ='Quantidade de vitórias por clube'
)

st.plotly_chart(grafico, use_container_width=True)

st.subheader('Valor dos times ao longo dos anos')

graficos_valores = px.line(
    df,
    x='Ano',
    y='Valor_total',
    color='Clubes',
    markers=True,
    title='Evolução do valor dos clubes'
)

graficos_valores.update_traces (marker_symbol='star')
st.plotly_chart(graficos_valores, use_container_width=True)
