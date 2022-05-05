
#soma = 1/(2**0) + 1/(2**1) + 1/(2**3) + ... + 1/(2**99)
soma = 0

n = 0

while n < 100:
    termo_geral = 1/(2**n)
    #soma1 = 1 * 1/2
    #soma2 =  soma1 * 1/2
    #soma3 = soma2 * 1/2
    #proximo = anterior * termo
    soma = termo_geral + soma
    #soma = termo * i + soma
    n = n + 1

print(soma) 