# whith open('churras.txt', 'r') as arq:
#     conteudo = arq.read()
# print(conteudo)

soma = 0
linhas = conteudo.split('\n')
for l in linhas:
    campos = l.split(',')
    nome = campos[0]
    qtd = int(campos[1])
    valor = float(campos[2])

    valor_item = qtd * valor
    soma +=qtd * valor
print(soma)