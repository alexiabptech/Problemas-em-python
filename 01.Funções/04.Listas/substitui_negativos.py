def zera_negativos(lista):
    #lista = []
    i = 0
    while i < len(lista):
        if lista[i] < 0:
            lista[i] = 0
        i+=1
    return lista  

def zera_negativos(lista_inteiros):
    nl = []

    for numero in lista_inteiros:
        if numero < 0:
            nl.append(0)
        else: nl.append(numero)
    return nl