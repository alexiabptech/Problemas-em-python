def agrupa_por_nacionalidade(dic_atletas):
    #Devolve um  dic com nomes separados por nacionalidade
    # dic = {'nome':{infos}}
    #o dic_novo = {'País': [nome dos atletas desse país]}
    #1)Cria novo dic
    dic_paises = {}
    
    for chave, valor in dic_atletas.items():
        nacionalidade = valor['nacionalidade']
        if nacionalidade not in dic_paises:
            dic_paises[nacionalidade] = [chave]
        else:
            dic_paises[nacionalidade] += [chave]
    return dic_paises
            
        