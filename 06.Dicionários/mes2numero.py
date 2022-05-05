#Esse dicionário aqui está guardando uma chave e um valor.
# A chave corresponde aos nomes, o valor corresponde aos numeros
# Eu estou dizendo: Olha, que mes voe quer? digite um nome
# e retorne o que está guardado nessa chave que vc digitou, ou seja, o numero do mês
meses = {
    'janeiro': 1,
    'fevereiro': 2,
    'março': 3,
    'abril': 4,
    'maio': 5,
    'junho': 6,
    'julho': 7,
    'agosto': 8,
    'setembro': 9,
    'outubro': 10,
    'novembro': 11,
    'dezembro': 12,

}

mes_dito = input('Qual o mes?')
mes_em_numero = meses[mes_dito] #Aqui eu disse, no dicionário de meses, pega o nome q eu digitei e me devolve o valor
print(mes_em_numero)