def pais_campeao(quadro):
    ouros = []
    maior_ouro = 0

    for pais, medalhas in quadro.items():
        if maior_ouro == medalhas['ouro']:
            ouros.append(pais)
        if maior_ouro < medalhas['ouro']:
            maior_ouro = medalhas['ouro']
            ouros = [pais]

    if len(ouros) == 1:
        return ouros[0]

    pratas = []
    maior_prata = 0
    for pais in ouros:
        if maior_prata == medalhas[pais]['prata']:
            pratas.append(pais)
        if maior_prata < medalhas[pais]['prata']:
            maior_prata = medalhas[pais]['prata']
            pratas = [pais]
    if len(pratas) == 1:
        return pratas[0]

    bronzes = []
    maior_bronze = 0
    for pais in pratas:
        if maior_bronze == medalhas[pais]['bronze']:
            maior_bronze = medalhas[pais]['bronze']
            bronzes = [pais]

    if len(bronzes) == 1:
        return bronzes[0]    
    return 'empate'

print(pais_campeao({
    'China': {
        'ouro': 20,
        'prata': 35,
        'bronze': 40 
    },
    'Canadá': {
        'ouro': 5,
        'prata': 15,
        'bronze': 20
    },
    'Estados Unidos': {
        'ouro': 25,
        'prata': 30,
        'bronze': 40
    },
    'Brasil': {
        'ouro': 10,
        'prata': 10,
        'bronze': 8
    }
}))

def pais_campeao(quadro):
    ouros = []
    maior_ouro = 0

    for pais, medalhas in quadro.items():
        if maior_ouro == medalhas['ouro']:
            ouros.append(pais)
        if maior_ouro < medalhas['ouro']:
            maior_ouro = medalhas['ouro']
            ouros = [pais]

    if len(ouros) == 1:
        return ouros[0]

    pratas = []
    maior_prata = 0
    for pais in ouros:
        if maior_prata == medalhas[pais]['prata']:
            pratas.append(pais)
        if maior_prata < medalhas[pais]['prata']:
            maior_prata = medalhas[pais]['prata']
            pratas = [pais]
    if len(pratas) == 1:
        return pratas[0]

    bronzes = []
    maior_bronze = 0
    for pais in pratas:
        if maior_bronze == medalhas[pais]['bronze']:
            maior_bronze = medalhas[pais]['bronze']
            bronzes = [pais]

    if len(bronzes) == 1:
        return bronzes[0]    
    return 'empate'