def menorValor(arr):
    menor = arr[0]
    menor_index = 0
    for i in range(0, len(arr)):
        if (menor > arr[i]):
            menor = arr[i]
            menor_index = i
    return menor_index

def selectionSort(arr: list[int]):
    newArray = []

    for i in range(0, len(arr)):
        indexMenor = menorValor(arr)
        newArray.append(arr[indexMenor])
        arr.pop(indexMenor)
    
    return newArray

resp = 1
posicao = 1
array = []

while (resp == 1):
    valor = int(input(f'Digite o valor da posicao {posicao} da lista: '))
    array.append(valor)
    posicao += 1
    resp = int(input('Deseja adicionar outro valor a lista? (Sim - 1)\nR: '))



print('Array original:')
for i in range(0, len(array), 1):
    print(array[i])

newArray = selectionSort(array)

print('Array ordenado com SelectionSort')
for i in range(0, len(newArray), 1):
    print(newArray[i])
