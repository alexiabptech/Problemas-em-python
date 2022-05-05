p1 = input('Já assistiu todos os filmes? ') 
p2 = input('Tem camiseta temática? ') 
p3 = input('Já se fantasiou de algum personagem?') 
p4 = input('Tem algumTem algum action figure/nave/etc?') 
p5 = input('Já foi no Galaxys Edge, o parque temático da franquia?') 


lista = [p1, p2, p3, p4, p5]
s = 0
for i in lista:
    if i == 'sim':
        s = s + 1
r = [ "Inocente",  "Inocente", "Padawan", "Jedi", "Jedi", "One with the Force"]
print(r[s])