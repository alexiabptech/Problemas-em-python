arq = open('08.Arquivos/teste.txt', 'r', encoding="utf-8") #Abrindo o formato em utf8 decodificando as strings com assento
content = arq.read()
arq.close()

print(content)
