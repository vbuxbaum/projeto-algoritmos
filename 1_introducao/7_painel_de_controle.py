class PainelDeControle:
    def __init__(self, temp_atual=0, temp_desejada=0):
        self.__temperatura_atual = temp_atual
        self.__temperatura_desejada = temp_desejada

    def ligar_forno(self):
        # Código do método
        pass

    def desligar_forno(self):
        # Código do método
        pass


painel_teste = PainelDeControle()
assert isinstance(painel_teste, PainelDeControle)
