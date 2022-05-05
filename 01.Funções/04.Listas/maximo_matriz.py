def encontra_maximo(m):
    maior = 0 
    for linha in m:
        for num in linha:
            if maior < abs(num):
                maior = abs(num)
    return maior

entrada = [
[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9]    
]