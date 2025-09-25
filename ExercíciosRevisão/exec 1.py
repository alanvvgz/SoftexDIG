while True:
    voto = int(input("Digite seu voto (10-A, 20-B, 30-C, 98-Nulo, 99-Branco): "))
    if voto in [10, 20, 30, 98, 99]:
        break
    print("Voto inválido, tente novamente.")

print(f"Voto registrado: {voto}")
