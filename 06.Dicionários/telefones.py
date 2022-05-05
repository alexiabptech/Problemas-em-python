'''#Lista de contatos
Faça um programa que pergunta o nome da pessoa
para o usuário e imprime o telefone
dessa pessoa. Se não souber o telefone
imprima "NOME não está na lista de ctts"
item = par {"chave" : "valor"}'''

telefones = { 
    "fulano": "9999-1111",
    "sicrano": "9999-2222",
    "beltrano":'9999-3333'
}
#print(telefones["sicrano"])
nome = input("Digite o nome: ")

telefone = telefones[nome]
print(telefone)

