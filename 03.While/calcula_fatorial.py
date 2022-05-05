def fatorial(n):
#o fatorial consiste em sucessivas multiplicaççoes de numeros em ordem decrescente
# 4! = 4 * 3 * 2 * 1
# n! = n * (n-1) * (n-2) * (n-3) ...

    i = 0
    fatorial = 1
    while i <= n:
        # fatorial[1] = fatorial[1]
        # fatorial[2] = fatorial[2] * fatorial[1]
        # fatorial[n] = fatorial[n] * fatorial[n-1]
        fatorial = fatorial*(n-i)
