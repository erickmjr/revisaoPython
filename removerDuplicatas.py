# Escreva uma função que receba uma lista e retorne uma nova lista
# com os elementos únicos, mantendo a ordem original.

def possuiValor(lista, item):
    for i in range(len(lista)):  
        if (lista[i] == item):
            return True
    return False

def removeDuplicatas(lista: list[int]):
    listaSemDuplicatas = []

    for i in range(len(lista)):
        duplicado = False

        for j in range(len(lista)):
            if ( (lista[i] == lista[j]) and i != j ):
                duplicado = True
                break

        if (duplicado and not possuiValor(listaSemDuplicatas, lista[i])):
            listaSemDuplicatas.append(lista[i])
            

    return listaSemDuplicatas


lista = [1, 1, 2, 2, 3, 3, 4, 4]

print(removeDuplicatas(lista))