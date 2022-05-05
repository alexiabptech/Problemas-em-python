def decodifica(codificada, trocas):
    destrocas = {}

    #a chave é como se fosse o i(posição)
    for chave in trocas:
        #valor do dic trocas == a chave do destrocas
        nova_chave = trocas[chave] #Corrreponde ao VALOR
        novo_valor = chave
        destrocas[nova_chave] = novo_valor
        
    string_nova = ''
    for letra in codificada:
        if letra in destrocas:
            string_nova = string_nova + destrocas[letra]#caso esteja, adiciona a do dicionário
        else:
            string_nova = string_nova + letra #em caso de a letra não estar no dic destrocas, apenas adc ela
    return string_nova
print(decodifica('eznznz'
,{
    'a': 'z',
    'b': 'e',
    'z': '!',
    'e': '*',
}))