def nota_quizzes(q1, q2, q3, q4, q5):
    #É necessário calcular a média de cada um, porém descartar a menor das 5
    #cria uma lista com cada nota
    #fixa uma nota pro for percorrer 
    #atualiza a variável para cada nota que o for percorrer
    #faz a média dentro da função e retorna ela
    
    lista = [q1, q2, q3, q4, q5]

    menor_nota = q1
    for quiz in lista:
        if quiz < 0 or quiz > 10:
            return 0
        if quiz < menor_nota:       
           menor_nota = quiz 

    med = (q1 + q2 + q3 + q4 +q5 - (menor_nota)) / 4

    return med 
print(nota_quizzes(5, 10, 10, 10, 10))