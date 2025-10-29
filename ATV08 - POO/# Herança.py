# Herança

# Exercício teórico — O que é herança:
# Herança é o mecanismo que permite criar uma classe (filha) que reutiliza atributos e métodos de outra (pai), possibilitando especializações sem repetir código. Exemplo do mundo real: Veículo (pai) e Carro / Bicicleta (filhas).

# Verdadeiro ou Falso:

# "( ) Uma classe filha herda apenas os métodos da classe pai, mas não os atributos." - Falso (herda ambos: atributos e métodos).

# "( ) O principal benefício da herança é evitar a repetição de código." - Verdadeiro.

# "( ) Em Python, uma classe pode herdar de múltiplas classes pai." - Verdadeiro.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Matrícula: {self.matricula}")

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Disciplina: {self.disciplina}")

if __name__ == "__main__":
    a = Aluno("Maria", 20, "20250123")
    p = Professor("Carlos", 45, "Matemática")
    a.exibir_dados()
    print("---")
    p.exibir_dados()
