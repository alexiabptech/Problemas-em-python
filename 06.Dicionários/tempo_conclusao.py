#Use: Tempo de conclusão 100 metros rasos (aula 8)

def calcula_tempo(atletas):
    for atleta in atletas:
        aceleracao = atletas[atleta]
        t = (200 / aceleracao) ** 0.5
        # t = delta_S / Velocidade
        atletas[atleta] = t
    return atletas

# Passo 1 - Cria dicionario de atletas
atletas = {}

# Passo 2 - Inicia loop do while para preencher o dicionário de atletas
continua = True
while continua:
    nome = input('Digite o nome do atleta: ')
    if nome == 'sair':
        continua = False
    else:
        aceleracao = float(input('Digite a aceleracao: '))
        # Passo 3 - Preenche dicionário de atletas
        atletas[nome] = aceleracao

# Passo 4 - Utiliza função auxiliar para preencher o novo dicionário
novo_atletas = calcula_tempo(atletas)

# Passo 5 - Percorre o dicionário acessar o nome do vencedor e o tempo (procurar o menor tempo, pois essa é a condição do vencedor)

referencia = min(novo_atletas.values())
for nome in novo_atletas:
    if novo_atletas[nome] == referencia:
        referencia_nome = nome
        # voce pode tirar (opcional)
        break

'''nomes_dos_atletas = list(novo_atletas.keys())
primeiro_nome = nomes_dos_atletas[0]
referencia = novo_atletas[primeiro_nome]
referencia_nome = primeiro_nome
for nome in novo_atletas:
    elemento = novo_atletas[nome]
    if elemento < referencia:
        referencia = elemento
        referencia_nome = nome'''

# Passo 6 - Mostra o vencedor
print(f'O vencedor é {referencia_nome} com tempo de conclusão de {referencia} s')