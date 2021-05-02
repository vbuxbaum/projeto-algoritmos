"""
Esta implementação em Java acusa o seguinte erro quando a entrada não possui
um numero par de elementos:

    java.lang.ArrayIndexOutOfBoundsException

Para contornar um erro semelhante em python, foi necessário utilizar o
seguinte artifício:

>>> proximo_indice = min(indice + 1, len(elementos) - 1)

"""


class MaxMin:
    @staticmethod
    def max_min_3(elementos):
        elementos, fim_anel = MaxMin.__define_anel(elementos)

        maximo, minimo = MaxMin.__inicializa_max_min(elementos)

        indice = 2
        while indice < fim_anel:
            proximo_indice = min(indice + 1, len(elementos) - 1)

            if elementos[indice] > elementos[proximo_indice]:
                if elementos[indice] > maximo:
                    maximo = elementos[indice]
                if elementos[proximo_indice] < minimo:
                    minimo = elementos[proximo_indice]
            else:
                if elementos[indice] < minimo:
                    minimo = elementos[indice]
                if elementos[proximo_indice] > maximo:
                    maximo = elementos[proximo_indice]
            indice += 2
        return (maximo, minimo)

    @staticmethod
    def __define_anel(elementos):
        fim_do_anel = 0
        num_elementos = len(elementos)
        if num_elementos % 2:
            fim_do_anel = num_elementos
        else:
            fim_do_anel = num_elementos - 1
        return elementos, fim_do_anel

    @staticmethod
    def __inicializa_max_min(elementos):
        max, min = 0, 0
        if elementos[0] > elementos[1]:
            max = elementos[0]
            min = elementos[1]
        else:
            max = elementos[1]
            min = elementos[0]
        return max, min


lista_strings = ["qwe", "mgh", "djf", "ois"]
lista_numeros = [2, 35, 843, 1, -45, 63, 11111]

assert MaxMin.max_min_3(lista_strings) == ("qwe", "djf")
assert MaxMin.max_min_3(lista_numeros) == (11111, -45)
