# Retirando a informacao de uma determinada base, mas nao no caminho correto

#from Estudo import func_x
# print (func_x)
# Este trecho apenas importa a parte da funcao do estudo '''

import pandas as pd
# import numpy as ny
import datetime as dt

db = pd.read_excel(r'Q:\FBR\Logistics\CONSULTAS E ACOMPANHAMENTOS\Planilhas de Acompanhamento\01 Planilhas de Acompanhamento - aéreo\Planilha_Acompanhamento_Huawei_AIR.xlsx')
print(db)

db['ETA Foxconn'] = db['ETA Foxconn'].dt.strftime('%d/%m/%Y')
df = db[['Reference', 'ETA Foxconn']].dropna()
print(db.dtypes)
print(db['ETA Foxconn'])
df.to_csv('Resultado.txt', index=False, header=False, sep='\t')
print (db)

# Comentarios gerais
# print(df('Chanel')) > dessa maneira ele nao entende o objeto como texto,
# por isso temos que usar o '[]'
# ANIMAL > print(VARIANTE.dtype) > demonstra qual e o tipo da variante
# Exemplos de conversao:
# db['ETA Foxconn'] = pd.to_datetime(db['ETA Foxconn'], format='%d / %m / %y')
# db['ETA Foxconn'] = db['ETA Foxconn'].apply(lambda x: x.strftime('%Y-%m-%d'))