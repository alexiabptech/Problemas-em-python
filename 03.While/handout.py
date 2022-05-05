# import random

# sorteio = random.randint(1,20)
# print(sorteio)

# chute = int(input('Advinhe o numero: '))

# if chute < sorteio:
#     print('Muito baixo')
# elif chute > sorteio:
#     print('Muito alto')
# else: 
#     print('Acertou')

tem_duvidas = True

if tem_duvidas:
    resposta_do_aluno = input('Você está com dúvidas? ')

    if resposta_do_aluno == 'não':
        print('Parabéns!')
        tem_duvidas = False
    else:
        print('Pratique mais')

