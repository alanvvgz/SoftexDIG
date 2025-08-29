idades = []

while True:
    idade = int(input("Digite uma idade (-1 para parar): "))
    if idade == -1:
        break
    idades.append(idade)

maiores = 0
for idade in idades:
    if idade >= 18:
        maiores += 1

print("Total de pessoas maiores de idade:", maiores)
