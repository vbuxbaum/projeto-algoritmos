"""
Nesta implementação em Java, o tipo genérico 'Item' implementa o método
compara() que é assegurado pela interface 'Item'.
Como o Python permite que seja feita a implementação do comparador '>' através
do magic method '__gt__', foi decidido pela sua utilização.
"""


class Max:
    def max(itens):
        item_max = itens[0]
        for item in itens[1:]:
            if item > item_max:
                item_max = item
        return item_max


if __name__ == "__main__":
    itens_teste_inteiro = [1, 2, 3, 4, 5]
    assert Max.max(itens_teste_inteiro) == 5

    itens_teste_string = ["zhiuh", "poas", "asd", "basd", "choi"]
    assert Max.max(itens_teste_string) == "zhiuh"
