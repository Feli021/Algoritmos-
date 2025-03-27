#Usando Numpy

import numpy as np

def diagonalDifference(arr):
    # Calcula a diferença absoluta entre as diagonais da matriz
    matriz = np.array(arr)
    soma_diagonal_principal = matriz.trace()
    soma_diagonal_secundaria = np.fliplr(matriz).trace()
    return abs(soma_diagonal_principal - soma_diagonal_secundaria)


if __name__ == "__main__":
    n = int(input().strip())

    arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

    result = diagonalDifference(arr)

    print(result)
 #Usando abordagem nativa do python (for)

def diagonalDifference(arr):
    """
    Calcula a diferença absoluta entre a soma da diagonal principal e da diagonal secundária.
    
    :param arr: Matriz quadrada (lista de listas)
    :return: Diferença absoluta entre as somas das diagonais
    """
    n = len(arr)
    soma_diagonal_principal = 0
    soma_diagonal_secundaria = 0

    for i in range(n):
        soma_diagonal_principal += arr[i][i]
        soma_diagonal_secundaria += arr[i][n - i - 1]

    return abs(soma_diagonal_principal - soma_diagonal_secundaria)


if __name__ == "__main__":
    n = int(input("Digite o tamanho da matriz: "))

    arr = []
    for _ in range(n):
        linha = list(map(int, input("Digite os elementos da linha separados por espaço: ").split()))
        arr.append(linha)

    result = diagonalDifference(arr)

    print(result)
