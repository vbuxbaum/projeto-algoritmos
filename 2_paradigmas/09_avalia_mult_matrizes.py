def main():
    numero_matrizes = coleta_numero_inteiro("Número de matrizes")
    dimensoes = coleta_dimensoes(numero_matrizes)
    matriz_de_resultados = matriz_de_zeros(numero_matrizes)

    print(f"\n{numero_matrizes = }, {dimensoes = }")
    print(f"\n{matriz_de_resultados = }")


def coleta_numero_inteiro(descricao):
    try:
        return int(input(f"{descricao}: "))
    except ValueError:
        print(
            "\nOoops, valor inválido!"
            f"\nPor favor digite um número inteiro para '{descricao}'.\n"
        )
        return coleta_numero_inteiro(descricao)


def coleta_dimensoes(numero_matrizes):
    return [
        coleta_numero_inteiro(f"Dimensão {indice} de {numero_matrizes}")
        for indice in range(numero_matrizes + 1)
    ]


def matriz_de_zeros(numero_matrizes):
    lista_de_zeros = [0 for _ in range(numero_matrizes)]

    return [lista_de_zeros for _ in range(numero_matrizes)]


if __name__ == "__main__":
    main()
