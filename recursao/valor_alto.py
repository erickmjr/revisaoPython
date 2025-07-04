def maiorValor(arr, Tarr):
    if (Tarr == 1):
        maior = arr[0]
        return maior

    

    if maiorValor(arr, Tarr-1) < :
        maior = arr[Tarr-1]
        return maior
    else:
        maior = arr[Tarr-2]
        return maior
    

    
print(maiorValor([1, 2, 3, 4, 5, 6, 67, 6, 2], 9))