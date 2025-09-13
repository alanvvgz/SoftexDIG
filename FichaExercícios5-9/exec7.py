numero = int(input("Digite um número: "))

listanumero = []

while True:
    listanumero.append(numero)
    
    if len(listanumero) == 7:
        print("O menor número digitado foi:", min(listanumero))
        break
    
    numero = int(input("Digite o próximo número: "))

