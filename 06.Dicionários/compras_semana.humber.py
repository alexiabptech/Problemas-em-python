def compras_da_semana(receitas,pratos):
    compras = {}
    for prato in pratos:
        #ver qual a receita do primeiro prato
        ingredientes = receitas[prato]
        for item, qtd in ingredientes.items():
            if item not in compras:
                compras[item] = qtd #maneira de adicionar a quantidade(chave)
            else:
              compras[item] += qtd  
    return compras