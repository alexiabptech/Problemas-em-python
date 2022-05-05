def total_do_semestre_por_bairro(gastos_por_bairro):
    ultimo6 = {}
    for bairro, gastos in gastos_por_bairro.items():
        # soma = 0
        # for mes in range(6,12):
        #     soma = soma + gastos[mes]
        soma = sum(gastos[6:12])
        
        
        ultimo6[bairro] = soma
    return ultimo6

