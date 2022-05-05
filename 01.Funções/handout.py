#Importando a Biblioteca:
#para calcular o cosseno de 0 
import math
resultado = math.cos(math.pi)
resultado = math.cos(0) 

noventa_em_radianos = 0.5 * math.pi
resultado = math.cos(noventa_em_radianos)
print(resultado)


#Cosseno recebe em radiano (Todos tan, sin, cos, etc, a biblioteca math recebe em radiano)
#print(resultado)

#Pensando no programa o que aconteceu 
# foi que plugamos uma caixa preta na 
# qual entram números representando angulos 
# e saem numeros representando o seu cosseno.
# 

def converte_milhas_para_km(distancia_mi):
    distancia_km = 1.60934 * distancia_mi
    return distancia_km

# Distancia_mi = argumento da função
# distancia_km = retorno ou resultado da função 
# as linhas 2 e 3 são o corpo ou bloco da função que estão dentro da identação

####

'''import conversoes #Na linha 1 queremos utilizar 
#funçoes disponiveis no arquivo conversoes

a = 10
b = conversoes.converte_milhas_para_km(a)
print(b)

#O valor da variavel a é utilizado, o python 
# b = conversoes.converte_milhas_para(10)
# b = 16.0934
# o valor 16.0934 é armazenado na variável b'''



 


