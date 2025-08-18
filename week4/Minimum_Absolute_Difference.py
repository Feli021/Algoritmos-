import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(arr):
    lista_ordenada = sorted(arr)
    menor_diff = float('inf')
     
    
    for i in range(len(lista_ordenada)):
        for j in range(i + 1, len(lista_ordenada)):
            diferenca = abs(lista_ordenada[i] - lista_ordenada[j])
            if diferenca < menor_diff:
                menor_diff = diferenca
                
                
    return menor_diff

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    result = minimumAbsoluteDifference(arr)

    

    
