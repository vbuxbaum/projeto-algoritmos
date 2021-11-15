'''Uso de lru_cache na função tenta()
> python3 06_passeio_cavalo.py CACHE_SIZE

O melhor valor de CACHE_SIZE nos testes foi 15'''


import sys
from timeit import timeit
from functools import lru_cache
from rich import print

MAX_CACHE = int(sys.argv[1])


class PasseioCavalo:
    PASSOS = [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
    ]

    def __init__(self, tamanho_tabuleiro, inicio=(0, 0)):
        self.tamanho_tabuleiro = tamanho_tabuleiro
        self.tabuleiro = [
            [0 for _ in range(tamanho_tabuleiro)]
            for _ in range(tamanho_tabuleiro)
        ]
        self.tabuleiro[inicio[0]][inicio[1]] = 1

        self.count_tenta = 0

    @lru_cache(maxsize=MAX_CACHE)
    def tenta(self, passo_n, pos_x, pos_y):

        self.count_tenta += 1
        for direcao in self.PASSOS:
            ctrl_sucesso = False

            pos_u = pos_x + direcao[0]
            pos_v = pos_y + direcao[1]

            if self.posicao_valida(pos_u, pos_v):
                self.preenche(passo_n, pos_u, pos_v)
                ctrl_sucesso = self.resolve_sucesso(passo_n + 1, pos_u, pos_v)
                if not ctrl_sucesso:
                    self.limpa(pos_u, pos_v)
            if ctrl_sucesso:
                break
        return ctrl_sucesso

    def resolve_sucesso(self, passo_n, x, y):
        if passo_n - 1 < self.tamanho_tabuleiro ** 2:
            return self.tenta(passo_n, x, y)
        else:
            return True

    def posicao_valida(self, x, y):
        return self.dentro_do_tabuleiro(x, y) and self.posicao_vazia(x, y)

    def dentro_do_tabuleiro(self, x, y):
        return x in range(self.tamanho_tabuleiro) and y in range(
            self.tamanho_tabuleiro
        )

    def posicao_vazia(self, x, y):
        return not self.tabuleiro[x][y]

    def preenche(self, passo_n, x, y):
        self.tabuleiro[x][y] = passo_n

    def limpa(self, x, y):
        self.tabuleiro[x][y] = 0


def main(N):
    p = PasseioCavalo(N)
    print(f"Começando com N = {N} e max_cache = {MAX_CACHE}")
    p.tenta(2, 0, 0)
    if p.tabuleiro:
        print("> > > count_ITER: " + str(p.count_tenta))
    p.tenta.cache_clear()


if __name__ == "__main__":

    for N in range(4, 8):
        print("> > > time: " + str(timeit(lambda: main(N), number=1)))
