import pandas as pd
import numpy as np
import os

'''
controle de diretório!
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
'''

abril = pd.read_excel(
    'C:/Projetos/PythonProject/CodigosEstudos/EstudoPandas/arq/Abril.xlsx')

print(abril.head())
