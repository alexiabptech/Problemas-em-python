'''
UTILIZANDO REFERÊNCIA
-Para pegar o menor elemento

lista = [0, 1, 10, -15, 20]

referencia = lista[0] (referencia de elemento)
referencia_i = 0 (referencia de posição)
for i in range(len(lista)):
    elemento = lista[i]
    if elemento < referencia:
        referencia = elemento
        referencia_i = i 
retorna o elemento e a posicao do menor elemento
-Em dicionarios acontece a mesma coisa, ou acessa chave ou valor,
guarda isso numa variavel referencia, que é o que vc quer comparar,
e atualiza
Ex:

nomes_dos_atletas = list(novo_atletas.keys())
primeiro_nome = nomes_dos_atletas[0]
referencia = novo_atletas[primeiro_nome]
referencia_nome = primeiro_nome
for nome in novo_atletas:
    elemento = novo_atletas[nome]
    if elemento < referencia:
        referencia = elemento
        referencia_nome = nome

------
'''
'''
QUADRO DE MEDALHAS POR REFERENCIA

def pais_campeao(quadro):
    #1)Cria referencias para cada comparação
    referencia_pais = ''
    referencia_ouro = -1
    referencia_prata = -1
    referencia_bronze = -1
    #Percorre o dicionario
    for pais in quadro:
        #Para cada pais, me de a qtd de medalhas
        medalhas_do_pais = quadro[pais] #medalhas é o valor (dicionario) dentro do quadro
        qtd_ouros = medalhas_do_pais['ouro']
        qtd_prata = medalhas_do_pais['prata']
        qtd_bronze = medalhas_do_pais['bronze']
        
        if qtd_ouros > referencia_ouro:
            referencia_pais = pais
            referencia_ouro = qtd_ouros
            referencia_prata = qtd_prata
            referencia_bronze = qtd_bronze
        
        elif qtd_ouros == referencia_ouro:
            if qtd_prata > referencia_prata:
                referencia_pais = pais
                referencia_prata = qtd_prata
                referencia_bronze = qtd_bronze
            elif qtd_prata == referencia_prata:
                if qtd_bronze > referencia_bronze:
                    referencia_pais = pais
                    referencia_bronze = qtd_bronze
    return referencia_pais
'''
'''
1) DOMINIOS DE TOPO (FATIAMENTO)
def usuarios_por_pais(lista_endereco, dic_dominio):

    #1 Cria um novo dicionario
    dic_novo = {}
    #2 Percorre a lista de usuarios
    
    for email in lista_endereco:
        #3 Faz o fatiamento do email para pegar o endereço com o nome de usuario
        
        lista_usu = email.split('@') #guarda numa lista,que vai ser separada antes e depois do @, pego e guardo numa nova variavel falando que quero a primeira posicao da lista com o endereço
        usuario = lista_usu[0] #usuario é o primeiro 
        
        #4 Splita a lista de endereços  separando agora o dominio (pais)
        
        lista_dominio = email.split('.')
        dominio = lista_dominio[-1] #pega a ultima posição que é onde está localizado o dominio
        
        #Extrai país do dominio, que está localizado no dicionario
        
        pais = dic_dominio[dominio] 

        #Preenche o novo dicionario com  cada áis como chave e a lista de usuarios como valor
        
        if pais not in dic_novo:
            dic_novo[pais] = []
        dic_novo[pais].append(usuario)

    return dic_novo

''' 

'''
RECEITA DE BOLO (SPLIT)

def converte_receita(receita):
    # receita = {'ingrediente(s)': qtd}
    # 1- Cria novo dicionario
    novo_dicionario = {}
    # #Percorre dicionario para acessar cada ingrediente

    for ingrediente in dic_receita:

        #Acessa o valor para pegar a quantidade de cada um

        qtde_do_ingrediente = dic_receita[ingrediente] 
        
        #A quantidade numerica vem na primeira posicao da string
        #Faz um split em que o separador é o espaço e pega só o numero
        
        qtde_numerica = int(qtde_do_ingrediente.split(' ')[0])
        
        #3 Depois de já ter separado cada coisa, agora precisamos testar as condições para cada ingrediente de acorod com a tabela de conversões
        
        if 'xícara' in qtde_do_ingrediente:
           
            #Se a string xicara, que ja engloba a que é no plural, corresponder às quantidades que ele dá, então adicoona no novo dicionário com sua respectiva conversão
           
            dic_novo[ingrediente] = str(250 * qtde_do_ingrediente) + 'ml'
        
        elif 'sopa' in qtde_do_ingrediente:
            dic_novo[ingrediente] = str(15 * qtde_numerica) + 'ml'
        
        elif 'chá' in qtde_do_ingrediente:
            dic_novo[ingrediente] = str(5 * qtde_numerica) + 'ml'
        
        #Se não é nenhum desses, é o ovo, que já retorna a propria quantdade numerica em forma de string
        
        else:
            dic_novo[ingrediente] = str(qtde_numerica)

    return dic_novo
    '''

'''
PREÇO DO COMBUSTÍVEL - ACESSANDO DIC POR PALAVRA FIXA

def contabiliza_combustivel(dic_combustivel):
    #1 Cria novo dicionario
    dic_novo = {}
    #2 Percorre dic_combustivel
    for chave, valor in dic_combustivel.items():
        #combustível vai ser o dicionário que corresponde ao valor da str 'diaX'
        combustivel = valor['tipo'] #valor é outro dicionario
        litro = valor['litros']
        custo = valor['custo']

        if combustivel not in dic_novo:
            #dic_novo[combustivel] = {'total litros': x, 'custo por litro' : y}

            dic_novo[combustivel]= {'total litros': litro, 'custo por litro' : custo}
        
        else: 
            dic_novo[combustivel]['total litros'] += litro

            dic_novo[combustivel]['custo por litro'] += custo 
    
    #Percorre o novo_dicionario e troca o que foi calculado pela média

    for chave, valor in dic_novo.items():
        total_litro = valor['total litros']
        total_custo = valor['custo por litro']
        total = total_custo/total_litro

        valor['custo por litro'] = total  
        
    return dic_novo

'''
'''
JOGO DE AVENTURA
def calcula_dano(dic_dano):
    # for valor in dic_dano.values():    
    #ou if chave == 'força': retorna isso
        forca = dic_dano['força'] #pega o valor da chave força
        #se o valor de quipamentos no diczão for vazio, retorna a força
        if dic_dano['equipamentos'] == []:
            return forca
        else: #se não tiver vazio, percorre a lista e procura a chave ['força'] e retorna a força 
            #somada para cada posição da lista
            for dicionario_i in dic_dano['equipamentos']:
                forca += dicionario_i['força']
            
            return forca 

def calcula_dano(dic_dano):
    for chave, valor in dic_dano.items():
        forca = valor['força']
        if dic_dano['equipamento'] == []:
            return forca
        else:
            for dicionario_i in dic_dano['equipamento']:
                forca += dicionario_i['força']
            
            return forca '''
'''
QUADRO DE MEDALHAS POR REFERENCIA

def pais_campeao(quadro):
    #1)Cria referencias para cada comparação
    referencia_pais = ''
    referencia_ouro = -1
    referencia_prata = -1
    referencia_bronze = -1
    #Percorre o dicionario
    for pais in quadro:
        #Para cada pais, me de a qtd de medalhas
        medalhas_do_pais = quadro[pais] #medalhas é o valor (dicionario) dentro do quadro
        qtd_ouros = medalhas_do_pais['ouro']
        qtd_prata = medalhas_do_pais['prata']
        qtd_bronze = medalhas_do_pais['bronze']
        
        if qtd_ouros > referencia_ouro:
            referencia_pais = pais
            referencia_ouro = qtd_ouros
            referencia_prata = qtd_prata
            referencia_bronze = qtd_bronze
        
        elif qtd_ouros == referencia_ouro:
            if qtd_prata > referencia_prata:
                referencia_pais = pais
                referencia_prata = qtd_prata
                referencia_bronze = qtd_bronze
            elif qtd_prata == referencia_prata:
                if qtd_bronze > referencia_bronze:
                    referencia_pais = pais
                    referencia_bronze = qtd_bronze
    return referencia_pais

'''
'''
- ATLETAS POR NACIONALIDADE -

Função que recebe um dic de atletas olimpicos
devolve nome de atletas separado por nacionalidade
se não tiver, coloca
se ja tiver, adiciona

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
            
        
'''
'''
- LISTA DENTRO DE LISTA - 
MATRIZ - PF
def eh_identidade(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            #Checa de é quadrada
            if len(matriz) != len(matriz[i]): #Tamanho a posição (linha [1,0,0])
            #len(matriz) = [ 0, 1, 2] cada elemento desse é uma sublista 
                return False
            
            if i == j and matriz[i][j] != 1: #[i][j] é a mesma posição
                return False

            if i != j and matriz[i][j] != 0:
                return False 
    return True
'''        
'''
- ACHE O WALLY- POSIÇÃO DENTRO DE LISTAS

def onde_esta_wally(matriz, ids):
    N = len(matriz)
    for i in range(N):
        for j in range(N):
            cpf = matriz[i][j]
            pessoa = ids[cpf]
            if pessoa == 'Wally':
                return [i, j]
        '''
'''
def filtra_bagagens(lista_bag, altural, largural, profundidadel):
    #DEvolve a quantidade de bagagens que excedem o limite
    #lista_nova = []

    #FAz um contador pra contar quantas bagagens não respeitam as condições propostas
    contador = 0 
    #percorre a lista de bagagens
    for i in range(len(lista_bag)):
        #define as posições que vão ser comparadas
        altura = lista_bag[i][0]
        largura = lista_bag[i][1]
        profundidade = lista_bag[i][2]
    #Compara com as dimensões dadas limites, se excede, conta
        if altura > altural:
            contador += 1

        elif largura > largural:
            contador += 1
        
        elif profundidade > profundidadel:
            contador += 1
    #depois de verificar tudo, retorna a quantidade de bagagens excedentes
    return contador
    '''
'''
-PEIXES
def categorias (categoria, dimensoes):
    dic_comp = {}
    dic_geral = {}
    for peixe, matriz in categoria.items():
        dic_comp[peixe] = []
        for lista in matriz:
            conta = ((dimensoes[0]-lista[0])*2+(dimensoes[0]-lista[0])2)*0.5
            dic_comp[peixe].append(conta)
            dic_geral[peixe] = min(dic_comp.values())

    #comparando:
    menor_valor = min(dic_geral.values())
    for peixe, valor in dic_geral.items():
        if valor == menor_valor:
            return 'O campeão é {0}'.format(peixe)'''


















