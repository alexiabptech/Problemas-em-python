estado = True  
lista = []

while estado:
    nome = input('Qual é o login : ')
    if nome == 'fim':
        estado = False  
        print('\n'.join(lista))               
    else: 
        novo = nome 
        i = 1 
        while novo in lista: 
            novo = nome + str(i)
            i += 1 
        lista.append(novo)