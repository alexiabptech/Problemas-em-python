def verifica_jogo_da_velha(t):
    #linhas
    lin = 0
    while lin < len(t):
        a = t[lin][0]
        b = t[lin][1]
        c = t[lin][2]
        if a != '.' and a==b and b==c:
            return a
        lin += 1
    #colunas
    col = 0
    while col < len(t[0]):
        a = t[0][col]
        b = t[1][col]
        c = t[2][col]
        if a != '.' and a==b and b==c:
            return a
        col += 1
    #diagonal principal
    if t[0][0] != '.' and t[0][0]==t[1][1] and t[1][1]==t[2][2]:
        return t[0][0]
    #diagonal secundaria
    if t[0][2] != '.' and t[0][2]==t[1][1] and t[1][1]==t[2][0]:
        return t[0][2]
    return 'V'