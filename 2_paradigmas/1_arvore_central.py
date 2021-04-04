class ArvoreBinaria:
    def __init__(self):
        self.raiz = self.No()

    def central(cls, no_pesquisado):
        if no_pesquisado is not None:
            cls.central(no_pesquisado.esquerda)
            print(no_pesquisado.valor)
            cls.central(no_pesquisado.direita)

    class No:
        def __init__(self):
            self.valor = None
            self.esquerda = None
            self.direita = None
