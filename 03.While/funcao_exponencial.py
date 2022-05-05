from math import *
def calcula_euler(x, n):
    #e**x = x**0/0! + x**1/1! + x**2/2! + x**3/3! ... 
    #termo_geral = x ** i/ factorial(i)
    soma = 0
    i = 0
    while i < n:
        termo_geral = (x ** i) / (factorial(i))
        soma = soma + (termo_geral)
        i = i + 1
    return(soma)
print(calcula_euler(2,2))
