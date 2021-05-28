# Some essa lista com comprehension

lista = []
lista.append(('Produto1', 20))
lista.append(('Produto2', 25))
lista.append(('Produto3', 20))

# desemp = [(x, y) for x, y in lista]  # Teste de desemacotamento
# print(desemp)


x = sum([y for x, y in lista])
print(x)
