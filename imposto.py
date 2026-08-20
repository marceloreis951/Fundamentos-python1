total = float(input("Digite o valor inteiro da NF: "))
pis = 0.0065
coffins = 0.03
csll = 0.01
vpis = float(total*pis)
vcoffins = float(total*coffins)
vcsll = float(total*csll)
liquido = total-vpis-vcoffins-vcsll
print(f"o valor total da NF é: {total}, o valor dos impostos são: PIS: {vpis:.2f}, COFFINS: {vcoffins:.2f}, CSLL: {vcsll:.2f}. O Valor Liquido na NF é: {liquido:.2f}")