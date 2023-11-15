from win32com.client.gencache import EnsureDispatch
from openpyxl import load_workbook
from pathlib import PurePath
import pandas as pd
import numpy as ny
import datetime as dt

def unprotect_wb_with_win32(file_dir_path, new_file_dir_path, password):
    xl_file = EnsureDispatch('Excel.Application')
    wb = xl_file.Workbooks.Open(file_dir_path, False, True, None, password)
    password = 'anazaula'
    wb.Unprotect(password)
    xl_file.DisplayAlerts = True
    wb.Visiable = True
    wb.SaveAs(new_file_dir_path, None, '', '')
    wb.Close
    xl_file.Quit()

if __name__ == '__main__':
    dir_path = r'C:\Users\renanalmeida\Desktop\Logistica'
    new_dir_path = r'C:\Users\renanalmeida\Desktop\Logistica\Output'
    file_name = 'Planilha_Acompanhamento_Huawei_SEA.xlsx'
    file_path = PurePath(dir_path, file_name)
    new_file_path = PurePath(new_dir_path, file_name)
    password = 'anazaula'

unprotect_wb_with_win32(str(file_path), str(new_file_path), password)


db = pd.read_excel(r'C:\Users\renanalmeida\Desktop\Logistica\Output\Planilha_Acompanhamento_Huawei_SEA.xlsx')
#db ['ETA Foxconn'] = pd.to_datetime(db['ETA Foxconn'], format='%d / %m / %y')
db ['ETA Foxconn'] = db['ETA Foxconn'].dt.strftime('%d/%m/%Y')
df = db[['Reference', 'ETA Foxconn']].dropna() 
#db ['ETA Foxconn'] = db['ETA Foxconn'].astype('string')
print(db.dtypes)
print (db ['ETA Foxconn'])

df.to_csv('Resultado.txt', index=False, header=False, sep = '\t')
