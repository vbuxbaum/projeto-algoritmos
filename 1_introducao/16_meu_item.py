class Item1(object):
    def __gt__(self, outro_item):
        raise NotImplementedError()


class MeuItem(Item1):
    def __init__(self, chave):
        self.chave = chave

    def __gt__(self, outro_item):
        return self.chave > outro_item.chave


if __name__ == "__main__":
    item_teste_1 = MeuItem(321)
    item_teste_2 = MeuItem(123)

    assert item_teste_1 > item_teste_2

    item_teste_3 = MeuItem('321')
    item_teste_4 = MeuItem('123')

    assert item_teste_3 > item_teste_4
