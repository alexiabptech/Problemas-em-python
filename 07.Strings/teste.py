# data = '09/09/1999'
# fatia = data[3:5]
# print(fatia)
lista_nova = []
lista = ["Ana", "Beatriz", "Jorge","Cecília", "João","Amanda", "Joana", "Lucas"]
for i in lista:
    if i[:1] ==  i+1[:1]:
        lista_nova[i] += [i]
print(lista_nova)
