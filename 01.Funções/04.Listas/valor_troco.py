def calcula_troco(valor, pago, notas):
    troco = pago - valor

    #notas = [20, 10, 5, 1]

    
    for nota in notas:
        qnota = troco // nota
        if qnota != 0:
            t = '{} notas'