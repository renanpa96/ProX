
import pandas as pd

db = pd.read_excel(r'Q:\FBR\Logistics\CONSULTAS E ACOMPANHAMENTOS\Planilhas de Acompanhamento\01 Planilhas de Acompanhamento - aéreo\Planilha_Acompanhamento_Huawei_AIR.xlsx')

db['ETA Foxconn'] = db['ETA Foxconn'].dt.strftime('%d/%m/%Y')
df = db[['Reference', 'ETA Foxconn']].dropna()
df.to_csv('Resultado.txt', index=False, header=False, sep='\t')
print(df)
