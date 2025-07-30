import math
import os
import random
import re
import sys

def pickingNumbers(a):
    # Creates a dictionary to store the frequency of each number
    frequencia = {}

    for num in a:
        if num in frequencia:
            frequencia[num] += 1
        else:
            frequencia[num] = 1

    # Lists the unique numbers in sorted order.
    numeros = sorted(frequencia.keys())
    max_sublista = 0

    # Checks consecutive pairs to form valid sublists
    for i in range(len(numeros) - 1):
        if abs(numeros[i] - numeros[i + 1]) <= 1: # CHECK if numbers are consecutive in value
            total = frequencia[numeros[i]] + frequencia[numeros[i + 1]]
            if total > max_sublista:
                max_sublista = total

    # Also consider the possibility that only one number repeats multiple times.
    max_sublista = max(max_sublista, max(frequencia.values()))

    return max_sublista
