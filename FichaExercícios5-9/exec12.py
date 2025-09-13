num = int(input("Digite um número: "))
tabini = int(input("Digite o número inicial da tabuada: "))
tabfim = int(input("Digite o número final da tabuada: "))

for i in range(tabini, tabfim + 1):
    print(f"{num} x {i} = {num * i}")
