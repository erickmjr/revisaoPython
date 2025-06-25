def verificaPalindromo(palavra, tamanhoPalavra):
    if tamanhoPalavra <= 1:
        return True
    if palavra[0].lower() != palavra[tamanhoPalavra - 1].lower():
        return False
    return verificaPalindromo(palavra[1:tamanhoPalavra - 1], tamanhoPalavra - 2)


def palindromo(palavra: str):
    palavraVerificada = ''
    for i in range(len(palavra) - 1, -1, -1):
        palavraVerificada = palavraVerificada + palavra[i]

    palavraVerificadaLower = palavraVerificada.lower()
    palavraLower = palavra.lower()
        
    return True if palavraVerificadaLower == palavraLower else False

palavra = 'radar'
print(verificaPalindromo(palavra, len(palavra)))