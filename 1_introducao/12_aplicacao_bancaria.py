"""
Nesta implementação em Java, o método imprime() lança Strings na saída padrão.
Para facilitar a implementação de testes, o comportamento desse método foi
alterado para que apenas retorne as respectivas Strings.
"""


class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def verifica_saldo(self):
        return "Saldo = $" + str(self.saldo)


conta_teste = ContaBancaria(200.00)

assert conta_teste.verifica_saldo() == "Saldo = $200.0"

conta_teste.depositar(50.00)
conta_teste.sacar(70.00)

assert conta_teste.verifica_saldo() == "Saldo = $180.0"
