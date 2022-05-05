agenda = {}
continuar = True
while continuar:
    nome = input('Nome:')
    tel = input('telefone:')
    if nome == '':
        continuar = False
    else:
        if nome not in agenda:
            agenda[nome] = []
        agenda[nome.append(tel)]

print(agenda)

del agenda['1berto']