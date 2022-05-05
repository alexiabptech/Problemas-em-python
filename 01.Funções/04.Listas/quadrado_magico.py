 def quadrado_magico(lista):

    soma = sum(lista[0])
    #Checar se as linhas dão a mesma soma
    for linha in lista[1:]:
        if sum(linha) != soma: 
            return False
    #Checar se as colunas dão a mesma soma
    colunas = []
    for i in range(len(lista)):
        coluna = 0 
        for linha in lista: 
            coluna += linha[i]
        colunas.append(coluna)
    for coluna in colunas:
        if coluna != soma:
            return False
    #Checar se as diagonais dão a mesma soma
    diagonal_principal = 0
    for i in range (len(lista)):
        diagonal_principal += lista[i][i]