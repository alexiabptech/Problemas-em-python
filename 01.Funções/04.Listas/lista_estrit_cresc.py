def estritamente_crescente(lista):
    if len(lista) == 0:
        return []
    
    nl = [lista[0]]
    for numero in lista:
        if numero : nl[len(nl)-1]