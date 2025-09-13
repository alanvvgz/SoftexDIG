num = int(input("Digite um número inteiro: "))

soma_div = 0

for i in range(1, num):
    if num % i == 0:
        soma_div += i


if soma_div == num:
    print(f"{num} é um número perfeito!")
else:
    print(f"{num} não é um número perfeito.")
