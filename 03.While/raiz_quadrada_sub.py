def raiz_quadrada(n):
    # sqrt(n) = quadrado perfeito
    # n = n - ímpar
    #loop pra contar de ímpar em ímpar, começando em 1 e indo de dois em dois
    conta_vezes = 0
    i = 1
    while i <= n:
        n = n - i
        i = i + 2
        conta_vezes += 1
    return conta_vezes

print(raiz_quadrada(49))