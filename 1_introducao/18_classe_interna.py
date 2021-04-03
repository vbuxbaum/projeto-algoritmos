class Lista:
    class Celula:
        pass


if __name__ == "__main__":
    lista_teste = Lista()
    celula_teste = Lista().Celula()

    assert isinstance(lista_teste, Lista), type(lista_teste)
    assert not isinstance(celula_teste, Lista), type(celula_teste)
    assert isinstance(celula_teste, Lista.Celula), type(celula_teste)
