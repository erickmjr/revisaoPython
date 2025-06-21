def tabuada(numero):
    for x in range(1, 11, 1):
        print(f'{numero} x {x} = {numero*x}')

valor = float(input('Digite um numero qualquer: '))

tabuada(valor)