import random
def cria_pecas(): 
#para i variando de 0 a 6, então devolva uma lista com todas as combinaçoes de 0 a 6 e um j fixo:
   lista_domino = []

   for i in range(0,7):
      for j in range(0,7):
         lista_peca = [i,j] #Varia primeiro o j até o 6 e depois volta pro primeiro for, variando o i
         lista_peca.sort()
         if lista_peca not in lista_domino: #Aqui eu estou dizendo que se a peca não está dentro da lista domino então adiciona 
            lista_domino.append(lista_peca)
   
   random.shuffle(lista_domino)
   return lista_domino 

def inicia_jogo(num_jog, lista_pecas):
    #funcao recebe numero de jogadores
    #recebe pecas a serem distribuidas
    #return dic={pecas:,monte}
    dic = {'jogadores':{}, 'monte':[], 'mesa':[]}

    if num_jog <= 4 and num_jog >=2: 
        for i in range(0, num_jog): #Aqui, eu to definindo um range da quantidade inicial 
            lista_7_pecas = []
            j = 0
            while j < 7: 
                lista_7_pecas.append(lista_pecas[j])   
                j = j + 1
            dic['jogadores'][i] = lista_7_pecas

            del(lista_pecas[0:7])

        dic['monte'] = lista_pecas
    return dic
def verifica_ganhador(num_jog):
    #num_jogadores = {numero: lista_peças}
    #return posicao do jogador sem peças
    for jogador, pecas in num_jog.items():
        if pecas == []:
            return jogador
        
    return -1

def soma_pecas(lista_pecas):
    #return pontos
    #lista_pecas=[[i,j]]
    soma = 0 
    for i in lista_pecas: # i = cada pecinha, para cada pecinha dentro da lista de pecas, percorra isso
        for j in i: # para cada pecinha percorra os elementos dela e guarde na variaavel soma
            soma = soma + j
    return soma 
        
def posicoes_possiveis(mesa, pecas):
    #cada peca tem uma das duas faces abertas quando colocadas na mesa
    #se tiver ao menos uma face igual
    #Quando a mesa ta vazia qqr peca pode ser colocada
    posiveis_pos = []
    if mesa == []:
        i = 0
        while i < len(pecas):
            posiveis_pos.append(i)
            i += 1
    else:
        i=0
        while i < len(pecas):
            if mesa[0][0] == pecas[i][0] or mesa[-1][1] == pecas[i][0] or mesa[-1][1] == pecas[i][1] or mesa[0][0] == pecas[i][1]:
                posiveis_pos.append(i)
            i += 1    
    return posiveis_pos

def adiciona_na_mesa(peca, mesa):
    #ex 1
    if len(mesa) == 0:
        mesa.append(peca)
        return mesa
    primeira_peca = mesa[0]
    ultima_peca = mesa[-1]
    #Se a primeira posicao da mesa for igual a segunda da peca na mão, então:
    #ex 2
    if primeira_peca[0] == peca[1]:
        mesa.insert(0, peca)
        return mesa
    #ex 4 
    if primeira_peca[0] == peca[0]:
        mesa.insert(0, [peca[1], peca[0]])
        return mesa
    #adiciona no final e inverte a peça
    if ultima_peca[1] == peca[1]:
        mesa.append([peca[1], peca[0]])
        return mesa
    #adiciona no final
    if ultima_peca[1] == peca[0]:
        mesa.append(peca)
        return mesa
 