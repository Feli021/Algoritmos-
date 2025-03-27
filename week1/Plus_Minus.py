import os

def plusMinus(arr):
    total = len(arr)
    
    # Inicializando as contagens
    positive_count = sum(1 for x in arr if x > 0)
    negative_count = sum(1 for x in arr if x < 0)
    zero_count = total - positive_count - negative_count  # O restante são zeros
    
    # Calculando as proporções
    positive_ratio = positive_count / total
    negative_ratio = negative_count / total
    zero_ratio = zero_count / total
    
    # Exibindo as proporções com 6 casas decimais
    print(f'{positive_ratio: .6f}')
    print(f'{negative_ratio: .6f}')
    print(f'{zero_ratio: .6f}')

