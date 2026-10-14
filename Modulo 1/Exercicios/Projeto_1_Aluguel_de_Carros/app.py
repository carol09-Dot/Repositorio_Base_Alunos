import streamlit as st

#------------------------------- SIDEBAR
st.sidebar.image ("logo.png")
st.sidebar.title("VeloClássicos - Aluguel de Carros")

carros = ["Chevrolet Opala", "Ford", "Mustang", "Chevrolet Impala", "Ford Maverick", "Volkwagen Fusca", "Cadillac DeVille", "Mercedes-Benz 280S", "Chevette"]
carro = st.sidebar.selectbox("Escolha seu carro:", carros)

#------------------------------- BODY
st.title("VeloClássicos - Aluguel de Carros")
st.image(f"{carro}.png")
st.write(f"Você alugou um {carro}")

dias = st.text_input(f"Por quantos dias você alugou o {carro}?")
km = st.text_input(f"Quantos km você rodou com o {carro}?")

if carro == "Chevrolet Opala":
    diaria = 800

elif carro == "Ford":
    diaria = 2.000

elif carro == "Mustang":
    diaria = 2.500

elif carro == "Chevrolet Impala":
    diaria = 800

elif carro == "Ford Maverick":
    diaria = 500

elif carro == "Volkwagen Fusca":
    diaria = 500

elif carro == "Volkwagen Fusca":
    diaria = 700

elif carro == "Cadillac DeVille":
    diaria = 850

elif carro == "Mercedes-Benz 280S":
    diaria = 1.500

elif carro == "Chevette":
    diaria = 900


if st.button("Calcular"):
    dias = int (dias)
    km = float (km)

    total = (dias * diaria) + (km * 0.15)

    st.warning(f"o total do aluguel a se pagar é R${total}.")