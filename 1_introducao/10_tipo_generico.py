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
        self.__tipo_de_item = tipo
        self.__primeira = self.Celula(self.__tipo_de_item)
        self.__ultima = self.Celula(self.__tipo_de_item)

    class Celula:
        def __init__(self, tipo=object):
            self.item = tipo()
            self.proximo = None
