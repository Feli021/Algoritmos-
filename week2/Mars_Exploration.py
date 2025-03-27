def marsExploration(s):
    """
    Conta quantas letras foram alteradas na transmissão de múltiplas mensagens "SOS".
    
    :param s: String recebida
    :return: Número de caracteres alterados
    """
    freq_de_letras_mudadas = 0
    expected = "SOS"

    for i in range(len(s)):
        if s[i] != expected[i % 3]:
            freq_de_letras_mudadas += 1

    return freq_de_letras_mudadas


if __name__ == "__main__":
    s = input("Digite a mensagem recebida: ")
    print(marsExploration(s))