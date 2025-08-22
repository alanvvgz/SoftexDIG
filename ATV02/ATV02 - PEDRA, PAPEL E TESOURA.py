import random

opcoes = ["pedra", "papel", "tesoura"]

usuario = input("Escolha (pedra, papel ou tesoura): ").lower()
computador = random.choice(opcoes)

print("Você escolheu:", usuario)
print("Computador escolheu:", computador)

if usuario == computador:
    print("Empate!")
else:
    if usuario == "pedra" and computador == "tesoura":
        print("Você venceu!")
    if usuario == "tesoura" and computador == "papel":
        print("Você venceu!")
    if usuario == "papel" and computador == "pedra":
        print("Você venceu!")
    if not (
        (usuario == "pedra" and computador == "tesoura") or
        (usuario == "tesoura" and computador == "papel") or
        (usuario == "papel" and computador == "pedra")
    ) and usuario in opcoes:
        print("Computador venceu!")
    if usuario not in opcoes:
        print("Opção inválida!")