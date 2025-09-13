cidadeA = 90000
cidadeB = 250000
taxaA = 0.035
taxaB = 0.012
anos = 0

while cidadeA <= cidadeB:
    cidadeA = cidadeA * (1 + taxaA)
    cidadeB = cidadeB * (1 + taxaB)
    anos = anos + 1

print(f"Levará {anos} anos para a população da cidade A ultrapassar a da cidade B.")