km1 = float(input("Digite o Km anterior: "))
km2 = float(input("Digite o Km atual: "))
rodado = km2-km1
litros = float(input("Digite quantos litros abasteceu: "))
media = rodado/litros
print(f"O KM anterior é: {km1:.2f} e o atual é: {km2:.2f}. A quantidade rodada foi de: {rodado:.2f}. Foi abastecido: {litros:.2f} e a média de litros por KM é: {media:.2f}")
