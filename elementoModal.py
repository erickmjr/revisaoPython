def contarOcorrencias(lista, alvo):
    aparicao = 0
    for i in range(len(lista)):
        if lista[i] == alvo:
            aparicao += 1
    return aparicao



def elementoModa(lista):

    maiorEncontrado = 0
    indexMaior = 0

    for i in range(len(lista)):
        ocorrenciasValor = contarOcorrencias(lista, lista[i])

        if (ocorrenciasValor > maiorEncontrado):
            maiorEncontrado = ocorrenciasValor
            indexMaior = i

    return ((lista[indexMaior], maiorEncontrado))


lista = [1, 1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 6]

print(elementoModa(lista))
