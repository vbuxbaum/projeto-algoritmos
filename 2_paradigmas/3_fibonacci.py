class Fibonacci:
    @classmethod
    def recursivo(cls, n):
        if n < 2:
            return n
        else:
            return cls.recursivo(n - 1) + cls.recursivo(n - 2)

    @classmethod
    def iterativo(cls, n):
        primeiro = 0
        segundo = 1
        for _ in range(n):
            primeiro = segundo + primeiro
            segundo = primeiro - segundo
        return primeiro


if __name__ == "__main__":
    teste_recursivo = Fibonacci.recursivo(7)
    teste_iterativo = Fibonacci.iterativo(7)

    assert teste_recursivo == 13
    assert teste_iterativo == 13
