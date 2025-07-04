posicao = 0
array = []
newArr = []
resp = 1

def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(0, len(arr), 1):
        if (arr[i] < menor):
            menor = arr[i]
            menor_indice = i
    return menor_indice

def selectionSort(arr):

    for i in range(0, len(arr), 1):
        menor = buscaMenor(arr)
        newArr.append(arr.pop(menor))
    return newArr



while (resp == 1):
    valor = int(input(f'Digite o valor da posicao {posicao} da lista: '))
    array.append(valor)
    posicao += 1
    resp = int(input('Deseja adicionar outro valor a lista? (Sim - 1)\nR: '))

selectionSort(array)
print('array ordenado: ')

for i in range(0, len(newArr)):
    print(f'{newArr[i]}')