def flippingBits(n):
    """
    Inverte os bits de um número de 32 bits e retorna o valor resultante.
    
    :param n: Número inteiro de 32 bits
    :return: Número com os bits invertidos
    """
    return ~n & 0xFFFFFFFF


if __name__ == "__main__":
    q = int(input("Digite a quantidade de casos de teste: "))

    for _ in range(q):
        n = int(input("Digite um número inteiro: "))
        print(flippingBits(n))