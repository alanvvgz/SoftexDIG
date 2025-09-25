n = int(input("Digite um número inteiro positivo: "))

while n < 0:
    n = int(input("Número inválido. Digite um inteiro positivo: "))

fatorial = 1
for i in range(1, n + 1):
    fatorial *= i

print(f"{n}! = {fatorial}")
