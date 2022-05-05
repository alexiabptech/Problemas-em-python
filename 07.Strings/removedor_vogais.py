def remove_vogais(texto):
    vogais = ['a', 'e', 'i', 'o', 'u']
    i = 0 
    while i < len(vogais):
        vogal = vogais[i]
        texto = texto.replace(vogal, '')
        i += 1    
    return texto


print(remove_vogais('abacaxi'))
print(remove_vogais('aoa'))
print(remove_vogais('kwyz'))

