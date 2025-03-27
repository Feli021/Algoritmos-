def countingValleys(steps, path):
    """
    Conta o número de vales percorridos durante uma caminhada.
    
    :param steps: Número total de passos
    :param path: Sequência de passos ('U' para subida, 'D' para descida)
    :return: Quantidade de vales percorridos
    """
    altitude = 0  # Nível do mar
    valleys = 0  # Contador de vales
    
    for step in path:
        if step == 'U':
            altitude += 1
        else:  # step == 'D'
            altitude -= 1

        # Se retornar ao nível do mar após uma subida, conta como um vale
        if altitude == 0 and step == 'U': 
            valleys += 1 
    
    return valleys


if __name__ == "__main__":
    steps = int(input("Digite o número total de passos: "))
    path = input("Digite a sequência de passos ('U' para subida, 'D' para descida): ")

    result = countingValleys(steps, path)

    print(result)