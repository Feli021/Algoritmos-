import sys
import re

def split_camel_case(text, is_method):
    """Splits a CamelCase name and returns words separated by spaces."""
    if is_method:
        text = text[:-2]  # Removes the parentheses at the end of the method
    words = re.findall(r'[A-Za-z][^A-Z]*', text)  # Splits words in CamelCase
    print(" ".join(words).lower())

def combine_to_camel_case(words, type_):
    """Combines space-separated words into a CamelCase name."""
    words = words.split()
    
    if type_ == "C":
        # Class names start with an uppercase letter
        camel_case = "".join(word.capitalize() for word in words)
    else:
        # Variable and method names start with a lowercase letter
        camel_case = words[0].lower() + "".join(word.capitalize() for word in words[1:])
    
    if type_ == "M":
        camel_case += "()"  # Methods end with ()
    
    print(camel_case)

# Reading input
for line in sys.stdin:
    operation, type_, text = line.strip().split(";")

    if operation == "S":
        split_camel_case(text, type_ == "M")
    elif operation == "C":
        combine_to_camel_case(text, type_)
