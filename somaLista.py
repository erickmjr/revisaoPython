# Soma de elementos de uma lista
# Dada uma lista de números, retorne a soma

posicao = 0
array = []
resp = 1

while (resp == 1):
    valor = float(input(f'Digite o valor da posicao {posicao} da lista: '))
    array.append(valor)
    posicao += 1
    resp = int(input('Deseja adicionar outro valor a lista? (Sim - 1)\nR: '))


nome = 'erick'
print(f'Soma de todos os valores presentes no array: {sum(array)}')
print(len(array))
print(len('erick'))
print(nome.split())

print(sorted(array))