def inverteString(string, tamanhoString):
    if tamanhoString == 0:
        return ''
    
    return string[tamanhoString-1]  + inverteString(string, tamanhoString - 1)

string = 'erick'

print(inverteString(string, len(string)))