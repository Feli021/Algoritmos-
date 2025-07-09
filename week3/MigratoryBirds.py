import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    contagem = {}

    # Count how many times each bird ID appears
    for i in arr:
        if i in contagem:
            contagem[i] += 1
        else:
            contagem[i] = 1

    # Find the highest number of sightings
    maior_valor = max(contagem.values())

    # Find all IDs with that highest number
    ids_com_maior_valor = []
    for k, v in contagem.items():
        if v == maior_valor:
            ids_com_maior_valor.append(k)

    # Return the smallest ID among the most frequently seen
    return min(ids_com_maior_valor)

    
    
    
if __name__ == '__main__':
   

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
