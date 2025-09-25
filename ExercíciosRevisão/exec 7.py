luz_acesa = False

while True:
    acao = int(input("O que fazer? (1: apertar interruptor, 0: sair): "))
    if acao == 0:
        print("Saindo...")
        break
    elif acao == 1:
        luz_acesa = not luz_acesa
    print("A luz está ACESA." if luz_acesa else "A luz está APAGADA.")
