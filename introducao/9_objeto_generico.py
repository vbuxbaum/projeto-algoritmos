class Lista:
    def __init__(self):
        self.__primeira = self.Celula()
        self.__ultima = self.Celula()

    class Celula:
        def __init__(self):
            self.item = object()
            self.proximo = self.Celula()
