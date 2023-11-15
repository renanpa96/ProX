# Retirando a informacao de uma determinada base, mas nao no caminho correto
# import numpy as ny
# import datetime as dt
# a planilha com senha da Huawei e a
import pandas as pd

# Planilha com o caminho teste de logistica >> db = pd.read_excel(
    #r'Q:\FBR\Logistics\CONSULTAS E ACOMPANHAMENTOS\Planilhas de Acompanhamento\01 Planilhas de Acompanhamento - aéreo\Planilha_Acompanhamento_Huawei_AIR.xlsx',
    #sheet_name='In Transit')

def unprotect_wb_with_win32(file_dir_path, new_file_dir_path, password):
    xl_file = EnsureDispatch('Excel.Application')
    wb = xl_file.Workbooks.Open(file_dir_path, False, True, None, password)
    password = 'anazaula'
    wb.Unprotect(password)
    xl_file.DisplayAlerts = True
    (((((((wb.Visiable))))))) = True
    db = pd.read_excel(
        r'C:\Users\renanalmeida\Desktop\Logistica\Planilha_Acompanhamento_Huawei_SEA.xlsx',
    sheet_name='In Transit'
    )
  
#Formatacao e Salvamento Txt
#db['ETA Foxconn'] = db['ETA Foxconn'].dt.strftime('%d/%m/%Y')
#df = db[['Reference', 'ETA Foxconn']].dropna()
#print(db.dtypes)
#print(db['ETA Foxconn'])
#df.to_csv('Resultado.txt', index=False, header=False, sep='\t')

'''
# Comentarios gerais
# print(df('Chanel')) > dessa maneira ele nao entende o objeto como texto,
por isso temos que usar o '[]'
# ANIMAL > print(VARIANTE.dtype) > demonstra qual e o tipo da variante
Exemplos de conversao:
#db['ETA Foxconn'] = pd.to_datetime(db['ETA Foxconn'], format='%d / %m / %y')
#db['ETA Foxconn'] = db['ETA Foxconn'].apply(lambda x: x.strftime('%Y-%m-%d'))
'''