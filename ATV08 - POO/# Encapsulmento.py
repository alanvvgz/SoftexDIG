# Encapsulamento

# Exercício teórico — Por que usar getters/setters?

# Evita acesso direto e descontrolado a atributos (protege consistência/integridade).

# Permite validações e regras (ex: impedir saldo negativo).

# Encapsula implementação; se no futuro mudar como o valor é armazenado, a interface pública continua a mesma.

# Convenção em Python para indicar atributo 'privado':
# Resposta: d) B e C são convenções usadas, mas com significados ligeiramente diferentes.

# _nome - convenção: tratado como “não público”.

# __nome - nome é mangled para evitar colisões em subclasses (name mangling).

class ContaBancaria:
    def __init__(self, saldo_inicial=0.0):
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial não pode ser negativo")
        self.__saldo = float(saldo_inicial)

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido. Deve ser positivo.")
            return False
        self.__saldo += valor
        print(f"Depósito de {valor:.2f} realizado. Saldo atual: {self.__saldo:.2f}")
        return True

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido. Deve ser positivo.")
            return False
        if valor > self.__saldo:
            print("Saldo insuficiente.")
            return False
        self.__saldo -= valor
        print(f"Saque de {valor:.2f} realizado. Saldo atual: {self.__saldo:.2f}")
        return True

    def get_saldo(self):
        return self.__saldo

if __name__ == "__main__":
    conta = ContaBancaria(100.0)
    conta.depositar(50)
    conta.sacar(30)
    print("Saldo final:", conta.get_saldo())
    
