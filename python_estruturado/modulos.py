# estudo de importar módulos
# lembrando que módulos podem estar dentro de pacotes!
# Módulos são arquivos .py que contem funções

# IMPORTANDO PACOTES

# import pacoteFuncoes.calculos
# Caso você faça o import dessa forma, você deverá chamar as funções do módulo
# da seguinte forma -->  print(pacoteFuncoes.calculos.somaDois(4))

# A forma correta é importar e dar um apelido para o import
# import pacoteFuncoes.calculos as calc
# Dessa forma, você importa tudo que há dentro do módulo.

# Para importal algo específico dos pacotes e módulos, você usa:
from pacoteFuncoes.calculos import somaDois, somaTres

# Formas de importar módulos
import funcao as func  # Dessa forma você importa TUDO o que existe no módulo
from funcao import mundo  # Dessa forma você importa apenas a função desejada


print(func.ola())
print(mundo())


# if __name__ == '__main__':
# O __name__ exibe o nome do módulo.
# Quando você esta executando o arquivo presente, o nome é sempre '__main__'.
# Entretanto, quando você importa o arquivo como módulo, o __name__ é realmente o nome do arquivo(módulo)
# Dessa forma, a gente usa do if __name__ == '__main__': para realizar blocos de testes dentro do módulo
# que não serão executados quando impotados em outro .py


# Nessa parte vou começar a usar o importe de pacotes !
# Já criei um pacote com dois módulos chamado "pacoteFuncoes"
# Dentro desse pacote, temos dois modulos -> calculos, exibicoes

print(somaDois(4))
