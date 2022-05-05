def compras_da_semana(receitas, pratos):
    lista_de_compras = {}
    # Percorre os pratos
    for prato in pratos:
        # Pega a receita dentro do dicionario de receitas
        receita = receitas[prato]
        # Percorre ingredientes na receita
        for ingrediente in receita:
            # Se ingrediente não estiver na lista de compra, adiciona o ingrediente
            if ingrediente not in lista_de_compras:
                lista_de_compras[ingrediente] = receita[ingrediente]
            # Se ingrediente estiver na lista de compra, soma o ingrediente no que ja existe
            else:
                lista_de_compras[ingrediente] += receita[ingrediente]
    return lista_de_compras