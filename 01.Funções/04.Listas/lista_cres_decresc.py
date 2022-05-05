def classifica_lista(lista):
    crescente = True
    decrescente = True
    for i in range(len(lista) - 1):
        if lista[i+1] > lista[i]:
            decrescente = False

        elif lista[i+1] < lista[i]:
            crescente = False
    
    if crescente and not(decrescente):
        return crescente
    if decrescente and not crescente:
        return decrescente