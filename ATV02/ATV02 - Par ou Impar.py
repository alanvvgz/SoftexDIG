while True:
    numero = int(input("Digite um número (ou -1 para sair): "))

    if numero == -1:
        print("Saindo...")
        break

    match numero % 2:
        case 0:
            print("O número é PAR")
        case 1:
            print("O número é ÍMPAR")
