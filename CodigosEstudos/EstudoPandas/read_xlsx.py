import pandas as pd
import numpy as np
import os
from sqlalchemy.engine import create_engine

# meu diretório padrão
DIR_DEFAULT = os.path.abspath(__file__)

# Nome do meu banco de dados
BANCO = 'SQLiteCorporeRM.db'
# string de conecção ao banco
str_banco = f'sqlite:///{os.path.join(os.path.dirname(os.path.dirname(DIR_DEFAULT)),BANCO)}'
# criando coneção
engine = create_engine(str_banco, echo=False)
# conectando ao banco de dados -> Criando banco
engine = engine.connect()

# DEFININDO DIRETÓRIO DO ARQUIVO EXCEL
DIR_DEFAULT = os.path.abspath(__file__)
DIR_ARQ = os.path.join(os.path.dirname(DIR_DEFAULT), 'arq', 'Abril.xlsx')

# LEITURA DA PLANILHA
abril = pd.read_excel(DIR_ARQ)

# TRANSFORMAÇÃO DO DATAFRAME EM TABELA NO BANCO DE DADOS
abril.to_sql('REPASSE', engine)
