
# 1) Olá Mundo Personalizado

nome = input("Por favor, digite o seu nome: ")
print(f"Olá, {nome}! Bem-vindo(a) ao mundo do Python!")


# 2) Calculadora Simples

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

print(f"A soma de {num1} e {num2} é: {num1 + num2}")
print(f"A subtração de {num1} por {num2} é: {num1 - num2}")
print(f"A multiplicação de {num1} por {num2} é: {num1 * num2}")
print(f"A divisão de {num1} por {num2} é: {num1 / num2}")


# 3) Informações do Produto

nome_produto = "Lápis"
preco_produto = 2.50
quantidade_estoque = 100

print(f"\nProduto: {nome_produto}")
print(f"Preço: R$ {preco_produto:.2f}")
print(f"Quantidade em estoque: {quantidade_estoque} unidades")


# 4) Calculadora de Área de Retângulo

altura = float(input("\nDigite a altura do retângulo (em metros): "))
largura = float(input("Digite a largura do retângulo (em metros): "))

area = altura * largura
print(f"A área do retângulo é de {area} metros quadrados.")


# 5) Conversor de Moedas (Simples)

cotacao_dolar = 5.25
valor_reais = float(input("\nDigite um valor em Reais (R$): "))

valor_dolares = valor_reais / cotacao_dolar
print(f"Com a cotação do dólar a R$ {cotacao_dolar}")
print(f"O valor de R$ {valor_reais:.2f} equivale a US$ {valor_dolares:.4f}")
