def colorindo(string, cores):
    # Tabela de cores - Usadas pela função "colorir"
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    YELLOW  = "\033[1;33m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[;7m"
    dicionario = {
        'vermelho': RED,
        'azul': BLUE,
        'ciano': CYAN,
        'amarelo': YELLOW,
        'verde': GREEN,
        'negrito': BOLD,
    }
    return dicionario[cores] + string + RESET

#string = 'oi'

# a funcao colorir receber dois argumento
# primeiro argumento: a string que vc quer colorir
# segundo argumento: a cor que vc quer colorir
# ela te retrona a string ja colorida
#print(colorindo(string, 'vermelho'))