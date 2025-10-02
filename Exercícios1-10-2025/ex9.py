num = [2, 5, 4, 1, 9]
def analisar_lista(numeros):
    soma = sum(numeros)
    maior = max(numeros)
    return (soma, maior)
resultado = analisar_lista(num)
print(resultado)
