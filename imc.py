# Autor: Marcelo Henrique 
# Proheto: Calculdora de IMC

print("=====Calculadora de IMC===== \n")

peso = float(input("Digite seu peso aqui: "))

altura = float(input("Digite sua altura aqui: "))

imc = peso / (altura*altura)

print(f"Seu IMC é: {imc:.2f}")

if imc <= 18.5:
   print("Precisa engordar!")
elif imc <= 25.0:
   print("Voce esta saudável.")
elif imc <= 30.0:
   print("Faça dieta!")
elif imc <= 35.0:
   print("faca academia!")
elif imc <= 40.0:
   print("Obesidade grau II")
else:
   print("Grau de obesidade III")