# Em poo, as "variaveis" são chamadas de atributos

class Pessoa():

    # Metodo __init__ é o costrutor da classe
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.meu_nome = nome
        self.minha_idade = idade
        self.comento = comendo
        self.falando = falando

    # o self quer dizer que é pra instancia pegar o metodo dela mesma
    def movimento(self, mov='Andando'):
        print(mov)
