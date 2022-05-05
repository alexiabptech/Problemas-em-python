def calcula_aumento(salario):

    if salario > (1250.00):
        aumento = (salario - 1250.00) * 1.1
        return aumento

    elif salario <= (1250.00):
        aumento = (salario - 1250.00) * 1.15 
        return aumento
print(calcula_aumento(1250.02))