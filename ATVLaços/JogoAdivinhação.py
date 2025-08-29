numero_secreto = 42
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número: "))

    if palpite < numero_secreto:
        print("Tente um maior")
    elif palpite > numero_secreto:
        print("Muito acima")

print("Parabéns, Você acertou!")
