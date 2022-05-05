def contabiliza_combustivel(dic_combustivel):
    #1 Cria novo dicionario
    dic_novo = {}
    #2 Percorre dic_combustivel
    for valor in dic_combustivel.values():
        combustivel = dic_combustivel[valor]

        if combustivel not in dic_novo:
            dic_novo[combustivel] = valor

            if 'litros' in dic_combustivel:
                dic_combustivel['litros'] = dic_novo['total litros'] 
                dic_novo['total litros'] += dic_novo['total litros']
            
            elif 'custo' in dic_combustivel:
                dic_combustivel['custo'] = dic_novo['custo por litro'] 
                dic_novo['custo por litro'] += (dic_novo['custo por litro'])/ dic_novo['total litros']
    
    return dic_novo
print(contabiliza_combustivel({
    'dia 1': {
        'tipo': 'Etanol',
        'litros': 20,
        'custo': 50.0
    },
    'dia 4': {
        'tipo': 'Gasolina',
        'litros': 25,
        'custo': 150.5
    },
    'dia 10': {
        'tipo': 'Gasolina',
        'litros': 15,
        'custo': 49.5
    },
    'dia 14': {
        'tipo': 'Etanol',
        'litros': 30,
        'custo': 70.0
    }}))