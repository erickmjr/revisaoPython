def somaDosElementosPares(lista): 
    soma = 0

    for i in range(0, len(lista)):
        if (lista[i] % 2 == 0):
            soma += lista[i]
    return soma

print(somaDosElementosPares([1, 455, 6, 5, 7, 8, 20]))