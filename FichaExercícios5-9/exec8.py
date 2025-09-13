produto = 1
soma = 0

numero = int(input("Digite um número: "))
listanumero = []

while True:
    listanumero.append(numero)
    
    if len(listanumero) == 6:
        break
    
    numero = int(input("Digite o próximo número: "))

for i in listanumero:
    produto = produto * i
    soma = soma + i

media = soma / len(listanumero)

print("Produto:", produto)
print("Média aritmética:", media)