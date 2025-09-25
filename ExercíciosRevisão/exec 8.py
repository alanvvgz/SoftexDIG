despesas = []

while True:
    valor = float(input("Digite uma despesa (0 para encerrar): "))
    if valor == 0:
        break
    if valor < 0:
        print("Valor inválido!")
        continue
    despesas.append(valor)

if despesas:
    total = sum(despesas)
    media = total / len(despesas)
    print(f"Total gasto: R$ {total:.2f}")
    print(f"Número de despesas: {len(despesas)}")
    print(f"Média por despesa: R$ {media:.2f}")
else:
    print("Nenhuma despesa registrada.")
