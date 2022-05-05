'''O professor de dessoft precisa de um sistema para automatizar
o cálculo de notas dos alunos, para isso, precisa desenvolver 
um sistema que recebe as notas de cada aluno num sistema 
e então calcula a nota final do semestre de cada aluno um a um
ao final do lançamento de todas as notas o programa imprime
a média geral da sala, assim como o percentual de alunos 
aprovados e o percentual de alunos reprovados

'''
'''
Q = média dos quizzess (a menor dos 5 é descartada)
Ni = 0.4 * AI + 0.5 * AF + 0.1 * Q
Ng = 0.1 * EP1 + 0.2 * EP2 + 0.7 * PF
Nf = (Ni + Ng)/2 if Ni >= 5 and Ng >= 5
Nf =  min(Ni, Ng) if Ni < 5 or Ng < 5
'''
''' Objetivos:
1)Pergunta se o usuário quer adc dados de mais um aluno
2) Pergunta as notas dos quizzes (1,2,3,4 e 5) na ordem 
3) Pergunta a nota da Ai
4)Pergunta a nota da Af
5)Pergunta anota do EP1
6)Pergunta a nota do EP2
7)Pergunta a nota do PF
8)Imprime a Nf com 'Nota final do anulo: NOTA' 
com duas casas decimais
9)Repete até que o usário digite 'não'
10)Imprime a média geral da sala, a média das NF com
'Média da sala: Média' com 2 casas decimais
11)Imprime o percentual de alunos aprovados com a mensagem:
'Aprovados: APROVADOS%' taxa de aprovados com 2 casas decimais
12)Imprime o percentual de alunos reprovados com: 'Reprovados: REPROVAODS%' 
com a taxa percentual 

'''