
import pandas as pd
import datetime as dt

filepath_huawei_air = r'Q:\FBR\Logistics\CONSULTAS E ACOMPANHAMENTOS\Planilhas de Acompanhamento\02 Planilha de acompanhamento - marítimo\Planilha_Acompanhamento_Huawei_SEA.xlsx'

db = pd.read_excel(filepath_huawei_air, sheet_name=['In transit '])

print(db['In transit '].columns['ETA Foxconn'])


db['ETA Foxconn'] = db['ETA Foxconn'].dt.strftime('%d/%m/%Y')
df = db[['Reference', 'ETA Foxconn']].dropna()
df.to_csv('Resultado.txt', index=False, header=False, sep='\t')

print(df)
