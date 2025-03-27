import os

def lonelyinteger(a):
    dicionario = {num: a.count(num) for num in a}  # Criando um dicionário com contagens
    for num, qtd in dicionario.items():  # Iterando sobre as chaves e valores do dicionário
        if qtd == 1:  # Se a quantidade for 1, retornamos o número
            return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))  # Lendo a lista de inteiros

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')
    fptr.close()
