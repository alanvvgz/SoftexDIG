num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
soma = 0

for i in range(num1, num2):
    if i % 2 != 0:
        soma = soma + i
print("Soma dos resultados: ", soma)