def filtra_bagagens(lista_bagagens, h_limite, l_limite, p_limite):
    numero_excedentes = 0
    for bagagem in lista_bagagens: # A variável tá assumindo o valo em cada teste
        h = bagagem[0]
        l = bagagem[1]
        p = bagagem[2]
        if h > h_limite or l > l_limite or p > p_limite:
            numero_excedentes += 1
        return numero_excedentes