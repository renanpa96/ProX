from win32com.client.gencache import EnsureDispatch
from openpyxl import load_workbook
from pathlib import PurePath



def set_wb_password_with_win32(file_dir_path, password):
    xl_file = EnsureDispatch("Excel.Application")
    wb = xl_file.Workbooks.Open(file_dir_path)
    xl_file.DisplayAlerts = False
    wb.Visiable = False
    wb.SaveAs(file_dir_path, Password = password)
    wb.Close()
    xl_file.Quit()

def unprotect_wb_with_win32(file_dir_path, new_file_dir_path, password):
    xl_file = EnsureDispatch("Excel.Application")
    wb = xl_file.Workbooks.Open(file_dir_path, False, True, None, password)
    wb.Unprotect(password)
    xl_file.DisplayAlerts = False
    wb.Visiable = False
    wb.SaveAs(new_file_dir_path, None,'','')
    wb.Close()
    xl_file.Quit()

if  __name__ == '__main__':
    dir_path = r'C:\Users\renanalmeida\Desktop\Logistica'
    file_name = 'Planilha_Acompanhamento_Huawei_SEA.xlsx'