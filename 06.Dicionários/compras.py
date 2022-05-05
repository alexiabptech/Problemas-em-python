compras = {
    'leite': 10,
    'ovo': 15,
    'carne':20
}

soma = 0 
for preco in compras.values():
    soma = soma + preco
print('O Total de compra é {0}'.format(soma))