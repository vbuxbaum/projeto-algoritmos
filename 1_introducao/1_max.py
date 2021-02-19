class Max:
    @staticmethod
    def max(elementos):
        valor_maximo = elementos[0]
        for valor in elementos[1:]:
            if valor > valor_maximo:
                valor_maximo = valor

        return valor_maximo


lista_strings = ["qwe", "mgh", "djf", "ois"]
lista_numeros = [2, 35, 843, 1, -45, 63, 11111, 0]

assert Max.max(lista_strings) == "qwe"
assert Max.max(lista_numeros) == 11111
