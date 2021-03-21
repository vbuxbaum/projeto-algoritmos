"""
Nesta implementação em Java, o livro utiliza o artifício de Generics.

Este artifício é importante para que linguagens estaticamente tipadas
consigam implementar novos tipos (classes) de forma genérica.

Como Python é dinamicamente tipada, esse tipo de artifício não é necessário
e podemos implementar classes genéricas a partir do Duck Typing.

Entretanto, uma forma de limitar o tipo dos elementos da lista implementada
segue abaixo
"""


class Lista:
    def __init__(self, tipo=object):
        self.tipo = tipo
        self.__primeira = self.Celula(self.tipo)
        self.__ultima = self.Celula(self.tipo)

        self.__primeira.proximo = self.__ultima

    def insere(self, elemento):
        if isinstance(elemento, self.tipo):
            nova_celula = self.Celula(self.tipo, elemento)
            nova_celula.proximo = self.__primeira.proximo
            self.__primeira.proximo = nova_celula
        else:
            raise TypeError(
                "Esta Lista apenas aceita elementos do tipo " + str(self.tipo)
            )

    def pega_primeiro(self):
        return self.__primeira.proximo

    class Celula:
        def __init__(self, tipo=object, valor=None):
            self.tipo = tipo()
            self.proximo = None
            self.valor = valor


lista_teste = Lista(int)
lista_teste.insere(32)

assert isinstance(lista_teste.pega_primeiro().tipo, int)

try:
    lista_teste.insere("Uma string qualquer")
except TypeError:
    pass
else:
    print("Era esperado um TypeError ao inserir uma String na classe Lista ")
