meus_nomes = [
    'jose_breaks.csv',
    'jordan_breaks.csv',
    'jhony_breaks.csv',
]

nova_lista = []
for x in meus_nomes:
    nova_lista.append(x.replace('_breaks.csv', ''))

print(nova_lista)
