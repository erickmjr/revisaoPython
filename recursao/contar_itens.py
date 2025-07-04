def contarItens(arr, Tarr):
    if Tarr == 1:
        return 1
    return 1 + contarItens(arr, Tarr - 1)

print(contarItens([1, 2, 34, 5, 6, 7], 6))