def miniMaxSum(arr):
    # Ordenando os números em ordem crescente
    arr.sort()
    
    # Calculando as somas das 4 menores e 4 maiores
    soma_menor = sum(arr[:4])  # soma das 4 menores
    soma_maior = sum(arr[1:])  # soma das 4 maiores
    
    print(soma_menor, soma_maior)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
