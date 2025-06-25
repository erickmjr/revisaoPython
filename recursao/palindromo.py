def verificaPalindromo(palavra, tamanhoPalavra):
    if tamanhoPalavra == 1:
        return True
    return ()


def palindromo(palavra: str):
    palavraVerificada = ''
    for i in range(len(palavra) - 1, -1, -1):
        palavraVerificada = palavraVerificada + palavra[i]

    palavraVerificadaLower = palavraVerificada.lower()
    palavraLower = palavra.lower()
        
    return True if palavraVerificadaLower == palavraLower else False

print(palindromo('SubiNoOnus'))