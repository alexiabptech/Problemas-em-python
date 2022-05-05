def conta_a(texto):
    i = 0
    contador = 0
    while i < len(texto):
        caractere = texto[i]
        if caractere == 'a':
            contador += 1
        i += 1
    return contador

quantoa_as = conta_a('abacaxi')
print(quantoa_as)