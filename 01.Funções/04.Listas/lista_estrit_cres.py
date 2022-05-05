def eh_crescente(lista):
    
    for i in range(len(lista)-1):
        if lista[i+1] <= lista[i]:
            return False
    return True
print(eh_crescente([2,1,3]))