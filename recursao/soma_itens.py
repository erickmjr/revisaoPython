def soma(arr, Tarr):
    if (Tarr == 1):
        return arr[0]
    return arr[Tarr-1] + soma(arr, Tarr-1)

print(soma([1, 2, 34], 3))