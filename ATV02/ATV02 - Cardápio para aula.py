cardapio = {
    1: ("Hambúrguer", 25.00),
    2: ("Batata Frita", 15.00),
    3: ("Refrigerante", 8.00),
}

total = 0

print("=== BEM-VINDO AO RESTAURANTE SANTA CRUZ FC ===")

while True:
    print("\n--- CARDÁPIO ---")
    for codigo, (item, preco) in cardapio.items():
        print(f"{codigo} - {item} - R${preco:,.2f}".replace(".", ","))

    print("0 - Finalizar pedido")

    escolha = input("Digite o código do item desejado: ")

    if not escolha.isdigit():
        print("Opção inválida! Digite apenas números.")
        continue

    escolha = int(escolha)

    if escolha == 0:
        break
    elif escolha in cardapio:
        item, preco = cardapio[escolha]
        total += preco
        print(f"Você adicionou: {item} - R${preco:,.2f}".replace(".", ","))
    else:
        print("Opção inválida!")

print("\n=== RESUMO DO PEDIDO ===")
print(f"Total a pagar: R${total:,.2f}".replace(".", ","))
print("Obrigado pela preferência! : )")

