import math
import os
import random
import re
import sys

def maximumPerimeterTriangle(sticks):
  sticks.sort(reverse=True)
  
  for i in range(len(sticks) - 2): 
    a, b, c = sticks[i], sticks[i+1], sticks[i+2]
    if (a + b > c and a + c > b and b + c > a):
        lados_ordenados = sorted([a, b, c])
        return lados_ordenados
        
 
  return [-1]
  
    
# len(sticks) - 2 -> I use this to ensure that I always form a group of 3 elements and do not go beyond the array's limits.

# a, b, c = sticks[i], sticks[i+1], sticks[i+2] -> I access three consecutive values from the list 'sticks' using their indices,
# and assign them to the variables a, b, and c. These represent the sides of a possible triangle.

# if (a + b > c and a + c > b and b + c > a): -> I check whether the three sides satisfy the triangle inequality,
# meaning they can form a valid (non-degenerate) triangle.

# lados_ordenados = sorted([a, b, c]) -> I sort the triangle sides in ascending order, as required by the problem.

# return lados_ordenados -> As soon as a valid triangle is found, I return the sorted list of its sides.

# return [-1] -> If no valid triangle can be formed, return [-1] as specified by the problem.

    
if __name__ == '__main__':

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)
