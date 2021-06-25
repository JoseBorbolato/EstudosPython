import pandas as pd
from ConexoesBanco import *

# PESQUISANDO TABELA GFILIAL E CRIANDO UM DATASET COM O RESULTADO DA PESQUISA
GFILIAL = pd.read_sql_query('select * from GFILIAL', conexaoSQLServer())
print(GFILIAL.head())
# CRIANTO UMA TABELA A PARTIR DO RESULTADO DO DATASET RETORNADO DO OUTRO BANCO DE DADOS
#GFILIAL.to_sql('GFILIAL', con=conexaoSQLite())
