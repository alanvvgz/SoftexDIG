def contar_vogais(texto):
    vogais = "aeiouAEIOUáÁéÉíÍóÓúÚâÂêÊôÔãÃõÕ"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

frase = "O incrível fenômeno da ciência revelou átomos, elétrons, íons e moléculas complexas."
print(contar_vogais(frase))
