print('\n')


# declaração da classe
class Pessoa:

    var_global = [1, 2, 3, 4, 5, 6]

    # Método construtor.
    # Executado toda vez que a classe é instanciada.
    # Quando você pede parâmetro no construtor, esses parâmetros vão ser
    # exigidos obrigatoriamente na hora de instanciar a clase.

    def __init__(self, nome='default', idade=0):
        self.nome = nome
        self.idade = idade
        self.cpf = '076.345.215.67'

    def nome_maiusc(self):
        self.nome = f'{self.nome.upper()} {self.cpf}'


if __name__ == '__main__':
    jose = Pessoa(nome='José Luiz Borbolato', idade=29)
    jose.nome_maiusc()
    print(jose.nome)
