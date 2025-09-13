numero = int(input("Digite um número inteiro: "))

if numero <= 2:
    print("O numero digitado não é um numero primo")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} não é primo")
            break
    else:
        print(f"{numero} é primo")