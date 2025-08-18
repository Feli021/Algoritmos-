import math
import os
import random
import re
import sys

def closestNumbers(arr):
    arr.sort()
    menor_diff = float('inf') 
    new_array = []   
    
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff < menor_diff:
            menor_diff = diff  
            
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == menor_diff:
            new_array.extend([arr[i], arr[i + 1]])
                                 
    return new_array
    
if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    
    

  
