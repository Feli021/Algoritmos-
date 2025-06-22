import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    #1 - Make all letters lowercase (ignore upper/lower case):
    s = s.lower()
    
    #2 - Create a set with the letters from your string
    letters_in_s = set(s)
    
    #3 - Create a set with the letters of the alphabet
    alphabet = set(string.ascii_lowercase)
    #'string.ascii_lowercase' represents a string with all lowercase letters of the English alphabet
    
    #4 - Filter only alphabet letters
    letters_in_s = set(c for c in s if c.isalpha())
    #isalpha() is a Python string method that checks whether all characters in a string are letters of the alphabet.
    
    #5 - Compare the sets
    if alphabet.issubset(letters_in_s):
        return "pangram"
    else:
        return "not pangram"
     #Explain '.issubset' -> A.issubset(B) = ""Are all elements of A inside B?"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
