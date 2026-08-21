#A utor: Marcelo Henrique 
# Projeto: Utilizando IF/ELIF/ELSE
# Operadores de comparação
# == igual
# != Diferente


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2

print(f"A média é: {media:.2f}")

if media >= 7:
    #/n Serve para pular uma linha
    print("Aluno aprovado! \n😊")
elif media <= 4:
    print("Aluno reprovado! \n😒")
else:
    print("Aluno recuperação! \n🤦")