def entregador_mais_proximo(lista_coord, lista_rest):

    lista_nova = []
    i = 0
    while i < len(lista_coord):
        calc = ((lista_coord[i][0] - lista_rest[0])**2 + (lista_coord[i][1] - lista_rest[1])**2)**0.5
        lista_nova.append(calc)
        
        i = i + 1   

    lista_f = lista_nova.index(min(lista_nova))
    
    return lista_f
print(entregador_mais_proximo([
    [10, 20],
    [4, 2],
    [100, 74],
    [23, 63]
]
, [3, 4]))