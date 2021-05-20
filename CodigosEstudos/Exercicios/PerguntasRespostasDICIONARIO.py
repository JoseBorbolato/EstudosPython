# exercício:
# Faça um sistema de perguntas e respostas usando dicionário.

dic = {
    'pergunta 01': {
        'pergunta': 'Qual a soma de 2 + 2?',
        'opcoes': {
            'A': 4,
            'B': 8,
            'C': 10,
            'D': 51,
            'E': 5
        },
        'resposta': 'A'
    },
    'pergunta 02': {
        'pergunta': 'Qual a soma de 2 + 6?',
        'opcoes': {
            'A': 4,
            'B': 8,
            'C': 10,
            'D': 51,
            'E': 5
        },
        'resposta': 'B'
    },
    'pergunta 03': {
        'pergunta': 'Qual a soma de 3 + 2?',
        'opcoes': {
            'A': 4,
            'B': 8,
            'C': 10,
            'D': 51,
            'E': 5
        },
        'resposta': 'E'
    }
}

nome = str(input('Olá, amigo. Qual é o seu nome? '))
nome = nome.split()
print(
    f'SEJA BEM VINDO AO NOSSO TESTE {nome[0].upper()}! RESPONDA NOSSAS PERGUNTAS:'
)

for chave, perguntasDados in dic.items():
    print(perguntasDados['pergunta'])
    for op, resp in perguntasDados['opcoes'].items():
        print(op, ')', resp)

    resposta = input('Qual a resposta certa ?  ')
    if resposta.upper() == perguntasDados['resposta'].upper():
        print('Parabéns, você acertou!!\n')
    else:
        print('Putz, você errou!\n')
