def calcula_media(dic_atletas, nome_pais):
    #cria_lista para guardar idade dos atletas
    lista_idades = []

    #Percorre dicionario de valores
    for valor in dic_atletas.values():
        nacionalidade = valor['nacionalidade']
        idade = valor['idade']
        if nacionalidade == nome_pais:
            lista_idades.append(idade)
            
    media = sum(lista_idades)/ len(lista_idades)    
    return media
    