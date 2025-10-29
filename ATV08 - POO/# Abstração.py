 # Abstração

 # Exercício teórico — Classe Livro (ponto de vista de um leitor):

 #                Atributos essenciais (3 exemplos):

# titulo — identifica o livro. Essencial para o leitor achar o exemplar.

# autor — informação importante ao escolher o livro.

# disponivel (booleano) — indica se pode pegar emprestado agora.

#                  Métodos essenciais (2 exemplos):

# emprestar() — marca o livro como não disponível; necessário para o fluxo de empréstimo.

# devolver() — marca como disponível; importante para controle.

# Por que são essenciais: o leitor precisa saber o que é o livro (título/autor) e se pode levá-lo (disponibilidade), enquanto métodos para emprestar/devolver modelam ações reais de um usuário da biblioteca.

# Questão de múltipla escolha:
 # Resposta: d) Ocultar a complexidade e expor apenas as funcionalidades essenciais de um objeto. 

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self._velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O carro está ligado.")
        else:
            print("O carro já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self._velocidade = 0
            print("O carro está desligado.")
        else:
            print("O carro já está desligado.")

    def acelerar(self, valor):
        if not self.ligado:
            print("Não é possível acelerar: o carro está desligado.")
            return
        if valor < 0:
            print("Valor de aceleração inválido.")
            return
        self._velocidade += valor
        print(f"Acelerou {valor} km/h. Velocidade atual: {self._velocidade} km/h.")

    def frear(self, valor):
        if valor < 0:
            print("Valor de frenagem inválido.")
            return
        self._velocidade = max(0, self._velocidade - valor)
        print(f"Freou {valor} km/h. Velocidade atual: {self._velocidade} km/h.")

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

if __name__ == "__main__":
    c = Carro("Toyota", "Corolla", 2020)
    c.exibir_informacoes()
    c.acelerar(20)  # carro desligado -> não acelera
    c.ligar()
    c.acelerar(30)
    c.frear(10)
    c.desligar()
