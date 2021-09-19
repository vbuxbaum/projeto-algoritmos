"""
Nesta implementação em Java, o método equivalente ao max_min() recebe 2
argumentos extras: um limite inferior e outro superior, para gerenciar o
'corte' da lista de números ao longo das recursões. Como o `slice` do Python é
uma ótima ferramenta para esse objetivo, ele foi adotado.

Além disso, a fim de deixar o método max_min() com menos responsabilidades,
foram criados os métodos decide_max() e decide_min(). E para possibilitar um
código mais enxuto, todos esses métodos viraram métodos de classe (ao invés de
estáticos, como na implementação em Java)
"""


class MaxMinRecursivo:
    @classmethod
    def max_min(cls, numeros):
        resultado_max_min = {}
        if len(numeros) == 1:
            resultado_max_min["max"] = resultado_max_min["min"] = numeros[0]
        elif len(numeros) == 2:
            resultado_max_min["max"], resultado_max_min["min"] = (
                numeros if numeros[0] > numeros[1] else numeros[::-1]
            )
        else:
            metade = len(numeros) // 2
            check_head = cls.max_min(numeros[:metade])
            check_tail = cls.max_min(numeros[metade:])
            resultado_max_min["max"] = cls._decide_max(check_head, check_tail)
            resultado_max_min["min"] = cls._decide_min(check_head, check_tail)
        return resultado_max_min

    @classmethod
    def _decide_max(cls, head, tail):
        return head["max"] if head["max"] > tail["max"] else tail["max"]

    @classmethod
    def _decide_min(cls, head, tail):
        return head["min"] if head["min"] < tail["min"] else tail["min"]


if __name__ == "__main__":
    primeira_rodada = MaxMinRecursivo.max_min(list(range(1, 13)))
    assert primeira_rodada == {"min": 1, "max": 12}

    segunda_rodada = MaxMinRecursivo.max_min([45, 32, 768, 98, 21, 9, 33])
    assert segunda_rodada == {"min": 9, "max": 768}
