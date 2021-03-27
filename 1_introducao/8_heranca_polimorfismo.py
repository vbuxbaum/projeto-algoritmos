"""
Nesta implementação em Java, o método imprime() lança Strings na saída padrão.
Para facilitar a implementação de testes, o comportamento desse método foi
alterado para que apenas retorne as respectivas Strings.

Nomes de classes foram alterados com fins de alcançar neutralidade de
gênero.
"""


class PessoaEmpregada:
    def __init__(self):
        self._salario = float()

    def salario_mensal(self):
        return self._salario

    def imprime(self):
        return "Pessoa Empregada"


class PessoaSecretaria(PessoaEmpregada):
    def __init__(self):
        super().__init__()
        self.__velocidade_de_digitacao = int()

    def imprime(self):
        return "Pessoa Secretaria"


class Gerente(PessoaEmpregada):
    def __init__(self):
        super().__init__()
        self.__bonus = float()

    def salario_mensal(self):
        return self._salario + self.__bonus

    # implementação 1.11:
    def salario_mensal(self, desconto):
        return self._salario + self._bonus - desconto

    # implementação 1.11 alternativa:
    #
    # def salario_mensal(self, desconto=0):
    #     return self._salario + self.__bonus - desconto

    def imprime(self):
        return "Gerente"


# Exemplo de polimorfismo

pessoa_empregada = PessoaEmpregada()
pessoa_secretaria = PessoaSecretaria()
gerente = Gerente()

assert pessoa_empregada.imprime() == "Pessoa Empregada"
assert pessoa_secretaria.imprime() == "Pessoa Secretaria"
assert gerente.imprime() == "Gerente"

assert isinstance(pessoa_secretaria, PessoaEmpregada)
assert isinstance(gerente, PessoaEmpregada)
