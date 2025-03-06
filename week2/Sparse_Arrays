def matchingStrings(strings, queries):
  
    frequency = {}

    for string in strings:
        frequency[string] = frequency.get(string, 0) + 1
    
    result = [frequency.get(query, 0) for query in queries]

    return result
