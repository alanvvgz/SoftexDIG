while True:
    nome = input("Digite seu nome: ")
    if len(nome) >= 3:
        print(f"Nome inserido com sucesso: {nome}")
        break
    else:
        print("Nome inválido! O nome deve ter pelo menos 3 caracteres.")

while True:
    idade = int(input("Digite sua idade: "))
    if idade > 0 and idade < 100:
        print(f"Idade inserida com sucesso: {idade}")
        break
    else:
        print("Idade inválida! Digite um valor entre 1 e 99.")

while True:
    salario = float(input("Digite seu salário: "))
    if salario >= 0:
        print(f"Salário inserido com sucesso: {salario}")
        break
    else:
        print("Salário inválido! Digite um valor positivo.")

while True:
    genero = input("Digite seu gênero (F/M/O): ").upper()
    if genero in ["F", "M", "O"]:
        print(f"Gênero inserido com sucesso: {genero}")
        break
    else:
        print("Gênero inválido! Digite F, M ou O.")

while True:
    situemp = input("Digite sua situação empregatícia (E - Empregado, D - Desempregado, A - Autônomo): ").upper()
    if situemp in ["E", "D", "A"]:
        print(f"Situação empregatícia inserida com sucesso: {situemp}")
        break
    else:
        print("Situação empregatícia inválida! Digite E, D ou A.")

print("\n==== Dados Cadastrados ====")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Gênero: {genero}")
print(f"Situação Empregatícia: {situemp}")
