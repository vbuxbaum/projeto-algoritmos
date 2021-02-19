class Max:
    @staticmethod
    def max(colecao):
        valor_maximo = colecao[0]
        for valor in colecao[1:]:
            try:
                if valor > valor_maximo:
                    valor_maximo = valor
            except TypeError:
                print(
                    "O método compara apenas elementos do mesmo tipo.\n"
                    + f"{type(valor_maximo)} é diferente de {type(valor)} "
                )
                return

        return valor_maximo


lista_strings = ["qwe", "mgh", "djf", "ois"]
lista_numeros = [2, 35, 843, 1, -45, 63, 11111, 0]
lista_mista = [2, 35, 843, 1, -45, "63", 11111, 0]

assert Max.max(lista_strings) == "qwe"
assert Max.max(lista_numeros) == 11111
assert Max.max(lista_mista) is None
