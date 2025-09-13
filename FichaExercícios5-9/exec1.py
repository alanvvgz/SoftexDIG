nota = int(input("Digite uma nota entre 0 e 5: "))

while True:
        if nota >= 0 and nota <= 5:
            print(f"Nota válida inserida: {nota}")
            break
        else:
            print("Nota invalida!")
            nota = int(input("Digite uma nota entre 0 e 5: "))
