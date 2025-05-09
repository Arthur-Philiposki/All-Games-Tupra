import streamlit as st
import random

st.title("Jogo: Pedra, Papel ou Tesoura")

opcoes = {
    1: "Pedra",
    2: "Papel",
    3: "Tesoura"
}

# Interface do usuário
escolha_usuario = st.radio("Escolha uma opção:", list(opcoes.values()))

# Botão para jogar
if st.button("Jogar"):
    # Obter número da escolha do usuário
    opcao_usuario = list(opcoes.keys())[list(opcoes.values()).index(escolha_usuario)]
    escolha_maquina = random.randint(1, 3)

    st.write(f"Você escolheu: **{opcoes[opcao_usuario]}**")
    st.write(f"A máquina escolheu: **{opcoes[escolha_maquina]}**")

    # Lógica do jogo
    if opcao_usuario == escolha_maquina:
        resultado = "Empate!"
    elif (opcao_usuario == 1 and escolha_maquina == 3) or \
         (opcao_usuario == 2 and escolha_maquina == 1) or \
         (opcao_usuario == 3 and escolha_maquina == 2):
        resultado = "🎉 Você Ganhou!"
    else:
        resultado = "😞 Você Perdeu!"

    st.subheader(resultado)
