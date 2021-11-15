"""É interessante mencionar que o Python já possui uma Estrutura de Dados
de listas (classe `list`) que, de certa forma, já realiza todas as operações
do exemplo do Livro. Entretanto vamos replicar a implementação para fins de
registro.

Vamos utilizar a estrutura 'array' do módulo Numpy do Python.

Ao invés de fazer a verificação de igualdade na *referencia* dos objetos, foi
feito verificando apenas igualdade de valor (operador ==)
"""

import numpy as np


class Lista:
    def __init__(self, max_tam):
        self.__item = np.empty(max_tam, dtype=object)
        self.__pos = -1
        self.__primeiro = self.__ultimo = 0

    def vazia(self):
        return self.__primeiro == self.__ultimo

    def pesquisa(self, chave):
        if self.vazia() or chave is None:
            return None

        for p in range(0, self.__ultimo):
            if self.__item[p] == chave:
                return self.__item[p]

        return None

    def insere(self, valor):
        if self.__ultimo >= len(self.__item):
            raise Exception("Erro: a lista está cheia")

        self.__item[self.__ultimo] = valor
        self.__ultimo += 1

    def retira(self, chave):
        if self.vazia() or chave is None:
            raise Exception(
                "Erro: a lista está vazia ou não aceita chave 'None'"
            )

        p = 0
        while p <= self.__ultimo and self.__item[p] != chave:
            p += 1

        if p >= self.__ultimo:  # Chave não encontrada
            return None

        item = self.__item[p]
        self.__ultimo -= 1
        for aux_p in range(p, self.__ultimo):
            self.__item[aux_p] = self.__item[aux_p + 1]

        return item

    def retira_primeiro(self):
        if self.vazia():
            raise Exception("Erro: a lista está vazia")

        item = self.__item[self.__primeiro]
        self.__ultimo -= 1

        for aux_p in range(self.__primeiro, self.__ultimo):
            self.__item[aux_p] = self.__item[aux_p + 1]

        return item

    def primeiro(self):
        self.__pos = -1
        return self.proximo()

    def proximo(self):
        self.__pos += 1
        return self.__item[self.__pos] if self.__pos < self.__ultimo else None

    def __str__(self) -> str:
        return ", ".join(
            str(self.__item[indice]) for indice in range(self.__ultimo)
        )


if __name__ == "__main__":
    lista = Lista(10)

    lista.insere("aaaaaaa")
    lista.insere({3: 4})
    lista.insere((3, 4))
    lista.insere(slice(1))

    lista.retira(slice(None, 1, None))
    lista.retira("slice")
    lista.retira({3: 4})
    lista.retira("aaaaaaa")
    lista.retira((3, 4))

    assert lista.vazia()
