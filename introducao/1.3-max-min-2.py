class MaxMin:
    @staticmethod
    def max_min_1(elementos):
        max = elementos[0]
        min = elementos[0]
        for valor in elementos[1:]:
            if valor > max:
                max = valor
            elif valor < min:
                min = valor

        return (max, min)


lista_strings = ["qwe", "mgh", "djf", "ois"]
lista_numeros = [2, 35, 843, 1, -45, 63, 11111, 0]

assert MaxMin.max_min_1(lista_strings) == ("qwe", "djf")
assert MaxMin.max_min_1(lista_numeros) == (11111, -45)
