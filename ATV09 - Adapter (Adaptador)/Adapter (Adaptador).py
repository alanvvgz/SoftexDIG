# Sistema antigo de pagamento
class SistemaPagamentoAntigo:
    def cobrar_no_cartao(self, valor_total, num_parcelas=1):
        print(f"[Sistema Antigo] Cobrando R${valor_total:.2f} em {num_parcelas} parcela(s).")


# Sistema novo de pagamento (interface esperada pelo cinema)
class SistemaPagamentoNovo:
    def pagar(self, valor):
        raise NotImplementedError("Método 'pagar' deve ser implementado.")


# Adaptador que conecta o novo sistema ao antigo
class AdaptadorPagamentoAntigo(SistemaPagamentoNovo):
    def __init__(self, sistema_antigo):
        self.sistema_antigo = sistema_antigo

    def pagar(self, valor):
        # Traduz o método 'pagar' (novo) para 'cobrar_no_cartao' (antigo)
        self.sistema_antigo.cobrar_no_cartao(valor_total=valor, num_parcelas=1)


# Exemplo de uso no cinema
if __name__ == "__main__":
    sistema_antigo = SistemaPagamentoAntigo()
    adaptador = AdaptadorPagamentoAntigo(sistema_antigo)

    # O cinema usa o método 'pagar', mesmo que o sistema antigo funcione diferente
    adaptador.pagar(50.00)




# O padrão Adapter é usado para fazer dois sistemas incompatíveis trabalharem juntos.
# No exemplo, o cinema usa um novo método pagar(valor), mas o sistema antigo só entende cobrar_no_cartao(valor_total, num_parcelas).
# O adaptador faz a tradução entre os dois formatos, permitindo que o novo sistema funcione sem precisar modificar o código antigo.