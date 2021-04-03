class Divisor:
    def divisao_except(a, b):
        try:
            if not b:
                raise Exception("Divisão por 0")
            return a / b
        except Exception as erro:
            return str(erro)

    def divisao_raise(a, b):
        if not b:
            raise Exception("Divisão por 0, raise externo")
        return a / b


if __name__ == "__main__":
    assert Divisor.divisao_except(3, 2) == 1.5
    assert Divisor.divisao_except(3, 0) == "Divisão por 0"

    try:
        Divisor.divisao_raise(3, 0)
    except Exception as erro:
        assert str(erro) == "Divisão por 0, raise externo", erro
