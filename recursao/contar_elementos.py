def contaElementos(lista):
    if lista == []:
        return 0
    return 1 + contaElementos(lista[1:])

lista = [1, 0, 4, 5, 6, 7]
print(contaElementos(lista))


# lista = [10, 20, 30, 40]
# print(lista[1:])  # [20, 30, 40]

# print(lista[:3])  # [10, 20, 30]

# print(lista[1:3])  # [20, 30]

# print(lista[:-1])  # [10, 20, 30]

# print(lista[::-1])  # [40, 30, 20, 10]
