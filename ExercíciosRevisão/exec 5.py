frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
cont_vogais = 0
cont_consoantes = 0

for char in frase:
    if char.isalpha():
        if char in vogais:
            cont_vogais += 1
        else:
            cont_consoantes += 1

print(f"Vogais: {cont_vogais}")
print(f"Consoantes: {cont_consoantes}")
