def calcula_extensao(x, y):
    #distancia = ((x2-x1)**2 + (y2-y1)**2)**0.5
    # x = [123, 321, 456]
    # y = [124, 453, 654]
    #return = cálculo com os indices ((x[1]-x[0])**2 + (y[0]-y[1]**2) **0.5
    i = 0
    soma = 0
    while i < len(x)-1:
        
        dist = ((x[i+1]- x[i])**2 + (y[i+1]- y[i]**2))**0.5
        soma =  soma + dist
        i = i + 1
    return dist
        
print(calcula_extensao([275, 290, 310, 390, 480] ,[75, 180, 120, 110, 150]))