# s = 'Engenharia Insper'
# so_insper = s[::2] #pula de 2 em dois
# print(so_insper) 2 = wuanto soma no insdice pra cehgar no q eu qro

# s = 'abababababa'
# a = s[1::2] #ou s[0:12:2] 
# print(a)

# s = 'Engenharia Insper'
# print(s[:]) #indices negativos voltam na string

# numeros = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numeros[2:5:])


# s = 'ola meu nome é toshi'
# palavras = s.split()
# print(palavras)
# tres_ultimas = palavras[-3:]
# print(tres_ultimas)
# junta_tudo = ' '.join(tres_ultimas)
# print(junta_tudo)

#concatena
texto = 'ola'
outro = 'pessoal'
texto= texto + outro
print(texto)

#Em lista é possivel alterar a posicao de um caractere
# lista = [1, 2, 3, 4]
# lista[1]=100
# print(lista)

#e se eu quiser trocar so uma letra na string?
texto = 'abcdb'
comeco = texto[:1]
final = texto[2:]
texto = comeco + 'Z' + final
print(texto)