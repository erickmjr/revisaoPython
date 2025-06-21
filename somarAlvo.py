# Escreva uma função que receba uma lista de inteiros e um número-alvo.
# Ela deve retornar todos os pares de números (índice diferente) cuja soma seja igual ao número-alvo.
# Ordem dos pares não importa, mas não pode ter repetições como (5, 2) se já teve (2, 5).

def possuiValor(lista, par):
    for i in range(len(lista)):
        if (lista[i] == par):
            return True
    return False

def somasAlvo(lista, alvo):
    pares = []

    for i in range(len(lista)):
        for j in range(i+1, len(lista)):

            if lista[i] + lista[j] == alvo and i != j :
                par = (min(lista[i], lista[j]), max(lista[i], lista[j]))

                if not possuiValor(pares, par):
                    pares.append((par))

    return pares

lista = [1, 3, 4, 2, 2, 6, 5, 7]

print(somasAlvo(lista, 7))