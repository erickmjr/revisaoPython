def indexMenorValor(lista):
    menor = lista[0]
    menorIndex = 0

    for i in range(0, len(lista)):
        if (menor > lista[i]):
            menor = lista[i]
            menorIndex = i

    return menorIndex    
    

def selectionSort(lista: list[int]):
    novaLista = []
    
    for i in range(0, len(lista)):
        menorIndex = indexMenorValor(lista)
        novaLista.append(lista[menorIndex])
        lista.pop(menorIndex)
    return novaLista


print(selectionSort([64, 34, 1, 45, 6, 2, 3, 5]))