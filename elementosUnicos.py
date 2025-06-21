# Dada uma lista de inteiros, crie uma função que retorne uma nova lista contendo apenas os elementos que aparecem exatamente uma vez na lista original.

def manterElementosUnicos(lista: list[int]):
    novaLista = []
    
    for i in range(len(lista)):
        duplicata = False  

        for j in range(len(lista)):
            if (lista[i] == lista[j] and i != j):
                duplicata = True

        if not duplicata:
            novaLista.append(lista[i])

    return novaLista
    
print(manterElementosUnicos([1, 3, 3, 5, 6, 6, 8]))
