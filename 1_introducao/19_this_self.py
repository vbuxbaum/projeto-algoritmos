"""
Nesta implementação em Java, o objetivo é ilustrar o uso do objeto 'this'. Em
Python, o objeto equivalente é 'self'.
"""


class Conta:
    def __init__(self, saldo):
        self.saldo = saldo


if __name__ == "__main__":

    conta_teste = Conta(123.45)

    assert conta_teste.saldo == 123.45
