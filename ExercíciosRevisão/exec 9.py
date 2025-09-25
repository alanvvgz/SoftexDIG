criancas = adolescentes = adultos = idosos = 0

for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    if idade <= 12:
        criancas += 1
    elif idade <= 17:
        adolescentes += 1
    elif idade <= 59:
        adultos += 1
    else:
        idosos += 1

print(f"Crianças: {criancas}")
print(f"Adolescentes: {adolescentes}")
print(f"Adultos: {adultos}")
print(f"Idosos: {idosos}")
