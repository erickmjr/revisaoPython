def encontraMaiorElemento(lista, tamanhoLista):
    if tamanhoLista == 1:
        return lista[0]
    
    maiorAtual = lista[tamanhoLista-1]
    maiorAnterior = encontraMaiorElemento(lista, tamanhoLista-1)

    if maiorAtual < maiorAnterior:
        maiorAtual = maiorAnterior
    return maiorAtual
        


print(encontraMaiorElemento([8000000, 3, 5, 6, 66, 60000000000000, 3, 912343223], 8))
