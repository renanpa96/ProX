import os
import win32com.client as win32

xls_app = win32.Dispatch('Excel.Application')
xls_app.Visible = True

wb = xls_app.Workbooks.Add()

wb.SaveAs(os.path.join(os.getcwd(),'NovoNomeda_Planilha.xlsx'))

# para recriar o nome da Aba, tem que declarar a Vairave e associar ao Nome da Aba original (Sheet1)
wb_sheet1 = wb.Worksheets('Sheet1')

wb_sheet1 = 'Primeira Aba'

wb_sheet1.Cells(1,'A').value = 'Sheet1'

