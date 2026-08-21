#Autor: Marcelo Henrqiue
#projeto: Motorista if/else and variáveis

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
carteira = True


# Estrutura condicional
# And -> todas as condições tem que ser verdadeiras

if idade >= 18 and carteira:
    print("Pode Dirigir")
else:
    print("Não pode dirigir")