while True:
    print("\n=== Comparação de Crescimento Populacional ===")

    while True:
        cidadeA = int(input("Digite a população inicial da Cidade A: "))
        cidadeB = int(input("Digite a população inicial da Cidade B: "))
        if cidadeA > 0 and cidadeB > 0:
            break
        else:
            print("As populações devem ser valores positivos!")

    while True:
        taxaA = float(input("Digite a taxa de crescimento anual da Cidade A (em %): ")) / 100
        taxaB = float(input("Digite a taxa de crescimento anual da Cidade B (em %): "))
        taxaB = taxaB / 100
        if taxaA > 0 and taxaB > 0:
            break
        else:
            print("As taxas de crescimento devem ser positivas!")

    anos = 0
    popA = cidadeA
    popB = cidadeB

    while popA <= popB:
        popA *= (1 + taxaA)
        popB *= (1 + taxaB)
        anos += 1

    print(f"\nCidade A ({cidadeA} hab., {taxaA*100:.2f}% ao ano)")
    print(f"Cidade B ({cidadeB} hab., {taxaB*100:.2f}% ao ano)")
    print(f"Levará {anos} anos para a população da Cidade A ultrapassar a da Cidade B.")
