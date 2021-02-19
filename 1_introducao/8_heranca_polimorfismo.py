class PessoaEmpregada:
    def __init__(self):
        self._salario = float()

    def salario_mensal(self):
        return self._salario

    def imprime(self):
        print("Pessoa Empregada")


class PessoaSecretaria(PessoaEmpregada):
    def __init__(self):
        super().__init__()
        self.__velocidade_de_digitacao = int()

    def imprime(self):
        print("Pessoa Secretaria")


class Gerente(PessoaEmpregada):
    def __init__(self):
        super().__init__()
        self.__bonus = float()

    def salario_mensal(self):
        return self._salario + self.__bonus

    def imprime(self):
        print("Gerente")


# Exemplo de polimorfismo

pessoa_empregada = PessoaEmpregada()
pessoa_secretaria = PessoaSecretaria()
gerente = Gerente()

pessoa_empregada.imprime()
pessoa_secretaria.imprime()
gerente.imprime()
