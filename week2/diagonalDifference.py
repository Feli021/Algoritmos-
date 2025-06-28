import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Check if the matrix is valid and if all rows have the same length
    n = len(arr)
    if n == 0 or any(len(row) != n for row in arr):
        return "Error: the matrix must be square (n x n)."
    
    principal_sum = 0
    secondary_sum = 0

    for i in range(n):
        principal_sum += arr[i][i]               # Main diagonal
        secondary_sum += arr[i][n - 1 - i]       # Secondary diagonal

    return abs(principal_sum - secondary_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
