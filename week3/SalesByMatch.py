import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
   contagem = {}
   total_pares = 0
   for valor in ar:
       if valor in contagem:
           contagem[valor] += 1
       else:
           contagem[valor] = 1
   
  
  
   for chave, qtd in contagem.items():
       num_de_pares = qtd // 2
       total_pares += num_de_pares
   return total_pares
  

if __name__ == '__main__':
    

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))
