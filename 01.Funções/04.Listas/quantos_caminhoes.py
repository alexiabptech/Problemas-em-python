def quantos_caminhoes(pcts):
    
    
    caminhoes = 0
    peso_caminhao = 0

    for pct in pcts:
        if (peso_caminhao + pct) >= 2000:
            caminhoes = caminhoes + 1
            peso_caminhao = 0
        peso_caminhao = peso_caminhao + pct
    if peso_caminhao > 0:
        caminhoes = caminhoes + 1
    return caminhoes