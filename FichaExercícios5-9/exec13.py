listanumpo = []
listanumneg = []
lista0 = []

for i in range(8):
    numero = int(input("Digite um número: "))
    if numero > 0:
        listanumpo.append(numero)
    elif numero < 0:
        listanumneg.append(numero)
    elif numero == 0:
        lista0.append(numero)

print("Total de números positivos: ", len(listanumpo))
print("Total de números negativos: ", len(listanumneg))
print("Total de 0: ", len(lista0))