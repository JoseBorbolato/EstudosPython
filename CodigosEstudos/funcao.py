# Aula de funções
# None também é um tipo de dado -> Não valor
# Quando a fução não encontra nenhum return, ela retorna None como padrão


def func(var='default'):
    return 'Valor do meu return'
    print(var)
    # todo código abaixo do 'return' não será executado.
    # Por esse motivo, o print(var) não vai exibir nenhum valor


# Função que retorna outra função.
# A função dump retorna uma outra função -> f

def f(msg='Default'):
    print(msg)


def dump():
    return f


'''
var = dump()
var()
'''


# Funções que recebem outras funções como parâmetros!
# O parênteses no retorno indica que será uma função.


def ola():
    return 'Olá'


def mundo():
    return 'Mundo'


def executafuncoes(funcoes):
    return(funcoes())


print(executafuncoes(ola))
print(executafuncoes(mundo))
