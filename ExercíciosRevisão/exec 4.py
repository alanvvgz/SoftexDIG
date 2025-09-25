qtd = int(input("Quantos alunos existem? "))
soma = 0

for i in range(qtd):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    while nota < 0 or nota > 10:
        nota = float(input("Nota inválida. Digite entre 0 e 10: "))
    soma += nota

media = soma / qtd
print(f"A média da turma é: {media:.2f}")
