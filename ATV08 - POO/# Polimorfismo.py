# Polimorfismo

# Exercício teórico — O que é polimorfismo?
# Polimorfismo significa "muitas formas": objetos de diferentes classes respondem ao mesmo método (mesmo nome) de formas específicas. No exemplo Pessoa, Aluno e Professor, todos tem exibir_dados() — mas cada classe implementa (ou estende) o método de maneira própria. Assim, você pode tratar todos como Pessoa e chamar exibir_dados() sem se preocupar com a implementação específica.

# Parte na pergunta “o que será impresso?” — (Se na lista havia um trecho específico, o comportamento típico é que o método da classe específica é chamado; sem o trecho exato, a explicação acima cobre o raciocínio.)

import csv

class ExportadorDeDados:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def exportar(self, dados):
        raise NotImplementedError("As classes filhas devem implementar exportar()")

class ExportadorParaCSV(ExportadorDeDados):
    def exportar(self, dados):
        
        if not dados:
            print("Nenhum dado para exportar.")
            return
        
        campos = list(dados[0].keys())
        with open(self.caminho_arquivo, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for row in dados:
                writer.writerow(row)
        print(f"Dados exportados para CSV: {self.caminho_arquivo}")

class ExportadorParaTXT(ExportadorDeDados):
    def exportar(self, dados):
        with open(self.caminho_arquivo, mode="w", encoding="utf-8") as f:
            for i, item in enumerate(dados, start=1):
                
                if isinstance(item, dict):
                    linhas = [f"{k}: {v}" for k, v in item.items()]
                    f.write(f"Registro {i}\n")
                    f.write("\n".join(linhas))
                    f.write("\n\n")
                else:
                    f.write(f"{item}\n\n")
        print(f"Dados exportados para TXT: {self.caminho_arquivo}")

def gerar_relatorios(exportadores, dados):
    for exp in exportadores:
        exp.exportar(dados)

if __name__ == "__main__":
    dados = [
        {"nome": "Alice", "idade": 30, "email": "alice@example.com"},
        {"nome": "Bruno", "idade": 25, "email": "bruno@example.com"},
    ]
    csv_exp = ExportadorParaCSV("usuarios.csv")
    txt_exp = ExportadorParaTXT("usuarios.txt")
    gerar_relatorios([csv_exp, txt_exp], dados)
