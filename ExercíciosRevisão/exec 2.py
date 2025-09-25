total = 0.0

while True:
    preco = float(input("Digite o preço do produto (0 para encerrar): "))
    if preco == 0:
        break
    if preco < 0:
        print("Preço inválido. Digite novamente.")
        continue
    total += preco

print(f"Total da compra: R$ {total:.2f}")
