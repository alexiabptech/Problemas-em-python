alunos = {
    'Humberto': {
        'ep1': 8,
        'ep2': 9,
        'ai': 5,
        'af': 4
    },
    'Doisberto': {
        'ep1': 8.5,
        'ep2': 2.3,
        'ai': 1.2,
        'af': 7
    } ,
    'Tresberto': {
        'ep1': 0.5,
        'ep2': 0.3,
        'ai': 8,
        'af': 5
    }    
}

media_sala = 0
for nome, notas in alunos.items():
    media = (notas['ep1'] + notas['ep2'] + notas['ai'] + notas['af']) / len(notas)
    media_sala += media
    print('{}: {}'.format(nome, media))