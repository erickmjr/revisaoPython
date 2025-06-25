def potencia(base, expoente):
    if base == 0:
        return 0
    if base == 1:
        return base
    if expoente == 0:
        return 1
    if expoente == 1:
        return base
    
    return base * potencia(base, expoente-1) 

print(potencia(10, 3))