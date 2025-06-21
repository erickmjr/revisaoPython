def parImpar(valor):
    return valor % 2 == 0

valorUsuario = int(input('Digite um numero inteiro: '))

if (parImpar(valorUsuario)):
    print(f'O numero {valorUsuario} eh par')
else:
    print(f'O numero {valorUsuario} eh impar')
