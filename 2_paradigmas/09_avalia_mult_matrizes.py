from rich import print


def main():
    numero_matrizes = coleta_numero_inteiro("Número de matrizes")

    matriz_de_resultados = preenche_custos(
        matriz_de_zeros(numero_matrizes), coleta_dimensoes(numero_matrizes)
    )

    imprime_matriz(matriz_de_resultados)


def coleta_numero_inteiro(descricao: str) -> int:
    try:
        return int(input(f"{descricao}: "))
    except ValueError:
        print(
            "\nOoops, valor inválido!"
            f"\nPor favor digite um número inteiro para '{descricao}'.\n"
        )
        return coleta_numero_inteiro(descricao)


def coleta_dimensoes(numero_matrizes: int) -> list:
    return [
        coleta_numero_inteiro(f"Dimensão {indice} de {numero_matrizes}")
        for indice in range(numero_matrizes + 1)
    ]


def matriz_de_zeros(numero_matrizes: int) -> list[list]:
    lista_de_zeros = [0 for _ in range(numero_matrizes)]

    return [lista_de_zeros.copy() for _ in range(numero_matrizes)]


def imprime_matriz(matriz: list[list]):
    if not matriz:
        print("Matriz vazia".center(80, "."))
        return

    print("[")
    for linha in matriz:
        print(f" {linha},")
    print("]")


def custos(matriz_de_zeros: list[list], dimensoes: list, i, j, k):
    return (
        matriz_de_zeros[i - 1][k - 1]
        + matriz_de_zeros[k][j - 1]
        + (dimensoes[i - 1] * dimensoes[k] * dimensoes[j])
    )


def preenche_custos(matriz_de_zeros: list[list], dimensoes: list):
    for h in range(1, len(matriz_de_zeros)):
        for i in range(1, len(matriz_de_zeros) - h + 1):
            j = i + h
            custo_atual = custos(matriz_de_zeros, dimensoes, i, j, i)

            for k in range(i + 1, j):
                custo_atual = min(
                    custo_atual, custos(matriz_de_zeros, dimensoes, i, j, k)
                )
            matriz_de_zeros[i - 1][j - 1] = custo_atual
            print(f"m[{i}][{j}] = {custo_atual}")
        print()
    return matriz_de_zeros


if __name__ == "__main__":
    main()
