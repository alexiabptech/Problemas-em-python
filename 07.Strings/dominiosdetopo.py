email = 'usuario1@email.insper.br'
usuario = email[:email.find('@')]
dominio = email[email.find('@')+1:]
partes = dominio.split('.')[-1]
print(usuario)
print(dominio)
print(partes[-1])


def usuarios_por_pais(emails, paises):
    saida = {}

    for email in emails:
        usuario = email[:email.find('@')]
        dominio = email[email.find('@')+1:]
        pais = dominio.split('.')[-1]
        nomepais = paises[pais]
        if nomepais not in saida:
            saida[nomepais] = usuario
            saida[nomepais].append(usuario)

    return saida