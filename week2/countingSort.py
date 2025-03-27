def countingSort(arr):
    """
    Retorna um array de frequência de 100 posições, onde cada índice 
    representa a quantidade de ocorrências do número correspondente em 'arr'.
    
    :param arr: Lista de inteiros a serem ordenados
    :return: Lista de frequência de tamanho 100
    """
    array_de_freq = [0] * 100  # Inicializa um array de frequência com 100 posições
    
    for num in arr:
        array_de_freq[num] += 1  # Conta a ocorrência de cada número
    
    return array_de_freq


if __name__ == "__main__":
    n = int(input("Digite a quantidade de elementos: "))
    arr = list(map(int, input("Digite os elementos separados por espaço: ").split()))

    result = countingSort(arr)

    print(" ".join(map(str, result)))
