''' << Here Importing modules for the cases bellow

from win32com.client.gencache import EnsureDispatch
from openpyxl import load_workbook
from pathlib import PurePath

HERE >> '''

''' << Here PROtect workbook

def set_wb_password_with_win32(file_dir_path, password):
    xl_file = EnsureDispatch('Excel.Application')
    wb = xl_file.Workbooks.Open(file_dir_path)
    xl_file.DisplayAlerts = False
    xl_file.Visible = False
    wb.SaveAs(file_dir_path, Password = password)
    wb.Close
    xl_file.Quit()
 
HERE >> '''

''' << Here unprotect workbook

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
    dir_path = 'planilhateste.xlsx'
    new_dir_path = r'C:\Users\renanalmeida\Desktop\My Docs'
    file_name = 'planilhateste.xlsx'
    file_path = PurePath(dir_path, file_name)
    new_file_path = PurePath(new_dir_path, file_name)
    password = 'anazaula'

unprotect_wb_with_win32(str(file_path), str(new_file_path), password)'''

''' << Here Exemplo colocando o caminho do arquivo de maneira correta

import openpyxl as opy
import pandas as pd
file_dir_path = r'C:\Users\renanalmeida\Desktop\My Docs\Sisfac 0700T.xlsx'

db = opy.load_workbook(file_dir_path)

#db = pd.read_excel(file_dir_path)

print(db)'''

# Huawei Air
import pandas as pd
import openpyxl as opy
from win32com.client.gencache import EnsureDispatch
from pathlib import PurePath

file_dir_path = r'C:\Users\renanalmeida\Desktop\My Docs\1) Melhorias\0) Python\Logistics\Logistica\Planilha_Acompanhamento_Huawei_AIR.xlsx'



def WB_Huawei_Air(file_dir_path, password):
    xl_file = EnsureDispatch('Excel.Application')
    wb = xl_file.Workbooks.Open(file_dir_path, False, True, None, password)
    wb.Unprotect(password)
    wb.DisplayAlerts = True
    wb.Visable = True

    

