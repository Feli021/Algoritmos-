def matchingStrings(strings, queries):
    """
    Conta quantas vezes cada string de 'queries' aparece na lista 'strings'.
    
    :param strings: Lista de strings fornecidas
    :param queries: Lista de strings a serem consultadas
    :return: Lista com a contagem de cada string em 'queries'
    """
    frequency = {}

    for string in strings:
        frequency[string] = frequency.get(string, 0) + 1

    result = []
    for query in queries:
        result.append(frequency.get(query, 0))

    return result


if __name__ == "__main__":
    strings_count = int(input("Digite a quantidade de strings: "))

    strings = []
    for _ in range(strings_count):
        strings.append(input("Digite uma string: "))

    queries_count = int(input("Digite a quantidade de consultas: "))

    queries = []
    for _ in range(queries_count):
        queries.append(input("Digite uma consulta: "))

    res = matchingStrings(strings, queries)

    for r in res:
        print(r)

