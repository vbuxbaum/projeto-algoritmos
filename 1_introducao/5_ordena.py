class Ordenador:
    @staticmethod
    def ordena(elementos):
        num_elementos = len(elementos)
        for i_externo in range(num_elementos - 1):
            minimo = i_externo

            for i_interno in range(i_externo + 1, num_elementos):
                if elementos[i_interno] < elementos[minimo]:
                    minimo = i_interno

            elementos[minimo], elementos[i_externo] = (
                elementos[i_externo],
                elementos[minimo],
            )


lista_strings = ["qwe", "mgh", "djf", "ois"]
lista_numeros = [2, 35, 843, 1, -45, 63, 11111, 0]

Ordenador.ordena(lista_strings)
Ordenador.ordena(lista_numeros)

assert lista_strings == ["djf", "mgh", "ois", "qwe"]
assert lista_numeros == [-45, 0, 1, 2, 35, 63, 843, 11111]
