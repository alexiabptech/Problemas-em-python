#Strings
# Quando vou somar uma string a outra usamos o termo "concatenar"
#Ctrl + alt
palavra = 'Insper'
print(palavra[0])
print(palavra[1])
print(palavra[2])
print(palavra[3])
print(palavra[4])
print(palavra[5])

#Métodos para string
#join
#find
#split
#replace
#strip

s = 'Engenharia Insper'
pos = s.find('Ins')
print(pos) #Printa a posição da string ins

#cria uma nova copia e devolve a nova copia
t = s.replace('Ins', 'Su') #substitui o ins por su
print(t) #
#aqui a variavel s continua com 'emg.. insper'
print(s)
t = s.strip()
print(t)
print(s)

# s = 'uma palavra outra palavra ultima palavra'
# print(s)
# separado = s.split() #o split  devolve uma lista de strings
# print(separado) #lista com 3 strings
# print(len(separado)) #primeiro elemeno de uma lista com strings
 

#Join - lista de strings
resultado = '<<<<|>>>>'.join(['a', 'b', 'c'])
print(resultado)
#list() pega a string e transforma numa lista com os caractteres separados

separado = resultado.split('<<<<|>>>>')
print(separado)







