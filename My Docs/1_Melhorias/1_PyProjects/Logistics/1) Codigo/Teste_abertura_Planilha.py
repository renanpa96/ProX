import pandas as pd
import openpyxl as opy
from win32com.client.gencache import EnsureDispatch
from pathlib import PurePath

#def WB_Huawei_Air(file_dir_path, password):
    #xl_file = EnsureDispatch('Excel.Application')
    #wb = xl_file.Workbooks.Open(file_dir_path, False, True, None, password)
    #wb.DisplayAlerts = True
    #wb.Visable = True
    # x = pd.read_excel(file_dir_path)
    # print('password')

file_dir_path = r'C:\Users\renanalmeida\Desktop\My Docs\1) Melhorias\0) Python\Logistics\Logistica\Planilha_Acompanhamento_Huawei_AIR.xlsx'
 
password = 'anazaula'


#WB_Huawei_Air(str(file_dir_path),password)
wb = pd.read_excel(file_dir_path)
print(wb)
print('oi')
