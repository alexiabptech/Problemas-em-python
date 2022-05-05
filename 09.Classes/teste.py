#classe = tipo do python
class Ponto:
    def __init__(self, valor_x, valor_y):
        self.x = valor_x
        self.y = valor_y

p = Ponto(5,3)
print(p.x)
print(p.y)
