class Lista:
    def __init__(self):
        self.__primeira = self.Celula()
        self.__ultima = self.Celula()

    class Celula:
        def __init__(self):
            self.item = object()
            self.proximo = None


lista_vazia = Lista()

assert isinstance(lista_vazia, Lista)
