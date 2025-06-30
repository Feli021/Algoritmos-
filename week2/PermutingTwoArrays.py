import math
import os
import random
import re
import sys
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B

def twoArrays(k, A, B):
 sorted_array = sorted(A) 
 reverse_sorted = sorted(B, reverse=True)
 
 for i in range(len(A)): 
 if sorted_array[i] + reverse_sorted[i] < k:
 return "NO"
 return "YES"

 # range(len(A)) creates the indices from 0 to len(A) - 1
 # for i in range(...) ensures that it will go through each index once 
 # If sorted_array[i] + reverse_sorted[i] < k, the condition is not met
