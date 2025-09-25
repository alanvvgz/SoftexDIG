while True:
    print("\n--- MENU BANCO ---")
    print("1. Ver Saldo")
    print("2. Fazer Depósito")
    print("3. Fazer Saque")
    print("4. Sair")

    opcao = int(input("Escolha: "))

    if opcao == 0 or opcao == 4:
        print("Saindo...")
        break
    elif opcao == 1:
        print("Você escolheu 'Ver Saldo'.")
    elif opcao == 2:
        print("Você escolheu 'Fazer Depósito'.")
    elif opcao == 3:
        print("Você escolheu 'Fazer Saque'.")
    else:
        print("Opção inválida!")
