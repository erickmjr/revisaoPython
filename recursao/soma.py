def somaRecursiva(lista, tamanhoLista):
    if tamanhoLista == 1:
        return lista[0]
    else:
        return lista[tamanhoLista-1] + somaRecursiva(lista, tamanhoLista - 1)


lista = [1,5,67,7]
tamanhoLista = len(lista)
print(somaRecursiva(lista, tamanhoLista))