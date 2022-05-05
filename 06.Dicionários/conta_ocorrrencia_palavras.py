# def conta_ocorrencia(palavras):
#     cont = {}
#     for palavra in palavras:
#         if palavra not in cont:
#             cont[palavra] = 1
#         else:
#             cont[palavra] += 1
#     return cont


def conta_ocorrencia(lista_palavras):
    dic = {}
    for palavra in lista_palavras:
        if palavra not in dic:
            dic[palavra] = 1
        else:
            dic[palavra] += 1
    return dic
        #   dic[palavra] = 0
        #dic[palavra] += 1

def mais_frequente(lista_palavras):
    dic_frequencia = conta_ocorrencia(lista_palavras)
    maior_valor = max(dic_frequencia.values())
    for palavra in dic_frequencia:
        if dic_frequencia[palavra] == maior_valor:
            return palavra 