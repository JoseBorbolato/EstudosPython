'''
================================================================================
Iterando sobre os dicionário com mais dicionários dentro =D
================================================================================
'''

cliente = {
    'C0001': {
        'Nome': 'José Luiz',
        'Idade': 29,
        'endereco': {
            'cep': '87301-320',
            'rua': 'Rua das acacias',
            'numero': 472,
            'cidade': 'Campo Mourão'
        }

    },
    'C0002': {
        'Nome': 'João Vitor',
        'Idade': 25

    },
    'C0003': {
        'Nome': 'Pedro Vandame',
        'Idade': 35,
        'endereco': {
            'cep': '87265-000',
            'rua': 'Rua andromeda',
            'numero': 51,
            'cidade': 'Quinta do Sol'
        }

    }
}

for codigo, dados in cliente.items():
    print(codigo)

    for chave, dados_pessoas in dados.items():
        print('\t', '->', dados_pessoas)
