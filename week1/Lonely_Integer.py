def lonelyinteger(a):
    
    dicionario = {num: a.count(num) for num in a}
    for num, qtd in dicionario.items():
        if qtd == 1:  
            return num
