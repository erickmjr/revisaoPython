def bubbleSort(array):
    troca = 0
    while (troca == 0):
        for i in range(0, len(array)-1, 1):
            aux = 0
            if (array[i] < array[i+1]):
                aux = array[i]
                array[i] = array[i+1]
                array[i+1] = aux
                troca = 0
            else:
                troca = 1

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

bubbleSort(array)

print('Array ordenado com BubbleSort')
for i in range(0, len(array), 1):
    print(array[i])

