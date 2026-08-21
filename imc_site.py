import streamlit as st

st.title("Calculadora de IMC")

st.write("Minha primeira página")

nome = st.text_input("Digite seu nome: ")

if st.button("Enviar"):
    if nome:
        st.success(f"Olá {nome} seja bem vindo!")
    else:
        st.warning("Gentileza, digitar seu nome!")

# python -m steamlit run