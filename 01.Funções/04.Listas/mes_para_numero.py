mes = input('Digite: ')
meses = ['janeiro', 'fevereiro' , 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'set', 'out', 'nov', 'dez']

i = 0 
while i < len(meses):
    if meses[i] == mes:
        print(i + 1)
    i = i + 1

#or print(meses.index(mes) + 1)