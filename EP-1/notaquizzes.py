'''A nota dos quizzes é feita pela 
média de 4 notas mas recebem 5 
argumentos, tendo que descartar o de
menor nota'''

def nota_quizzzes(q1, q2, q3, q4, q5):
    #É necessário calcular a média de cada
    #um porém descartar a menor das 5
    if q1 < 0 and q1 > 10 and q2 < 0 and q2 > 10 and q3 < 0 and q3 > 10 and q4 < 0 and q4 > 10 and q5 < 0 and q5 > 10:
        return 0

    if q1 < q2 and q1 < q3 and q1 < q4 and q1 < q5:
        med = (q2 + q3 + q4 + q5) / 4
        return med

    if q2 < q3 and q2 < q1 and q2 < q4 and q2 < q5:
        med = (q1 + q3 + q4 + q5) / 4
        return med

    if q3 < q4 and q3 < q2 and q3 < q5 and q3 < q1:
        med = (q1 + q2 + q4 + q5) / 4
        return med

    if q4 < q5 and q4 < q3 and q4 < q2 and q4 < q1:
        med = (q1 + q3 + q2 + q5) / 4
        return med

    if q5 < q4 and q5 < q3 and q5 < q2 and q5 < q1:
        med = (q1 + q3 + q4 + q2) / 4
        return med


print(nota_quizzzes(5, 0, 0, 0, 5))