class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def verifica_saldo(self):
        return "Saldo = $" + str(self.saldo)


conta_teste = ContaBancaria(100)

conta_teste.depositar(30)
conta_teste.sacar(20)

assert conta_teste.verifica_saldo() == "Saldo = $110"
