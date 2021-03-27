"""
Nesta implementação em Java, o livro utiliza o artificio 'static' da linguagem.
Entretanto não há uma forma, em Python, para simular o comportamento de
atributos estáticos EXATAMENTE como ocorre em Java.

Para simular o comportamento em Python, o atributo estático deve ser acessado
diretamente por sua classe, e não pela instância (como é feito no livro).
"""


class A:

    STATIC = int()

    def __init__(self):
        self.media = int()


a = A()
A.STATIC, a.STATIC, a.media = 5, 5, 5

b = A()
A.STATIC, b.STATIC, b.media = 7, 7, 7


assert (A.STATIC, a.STATIC, a.media, b.STATIC, b.media) == (7, 5, 5, 7, 7)
