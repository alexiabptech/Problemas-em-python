def calcula_pi(n):
    #retorns o resultado do pi
    #termo = 6/(i**2)

    soma = 0
    for i in range(1, n + 1):
        termo = 6/(i**2)
        soma = soma + termo 
    pi = soma ** 0.5
    #Vale ressaltar que o for soma todos os termos e o que queremos é a soma dos termos dentro da raiz
    return pi
