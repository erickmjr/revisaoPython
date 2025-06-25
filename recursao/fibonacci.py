def fib(elemento):
    if elemento == 1:
        return 0
    if elemento == 2:
        return 1
    
    return fib(elemento-1) + fib(elemento-2)

print(fib(12))
    