# '''Para as INVs, devemos tarbalhar dentro as colunas (concat. PN  Qty e extraindo do  nome do arquivo o num da invoice)'''


import pandas as pd

#wb = openpyxl.load_workbook(r'C:\Users\renanalmeida\Desktop\My Docs\1) Melhorias\TVC23000183 BXDGZ-23010空运联络单-巴西富士康-5.xlsx')
#wbs = wb.create_sheet("Invoices",0)
#wbs.save ('TVC23000183')

#print(wb.sheetnames)
#new_wb = wb.save('Inovoice1')
#ws = wb.worksheets[0]
#warn("""Cannot parse header or footer so it will be ignored""") > colocar o read_only=true que da bom
#ws.print_titles

wb = pd.read_excel(r'C:\Users\renanalmeida\Desktop\My Docs\1) Melhorias\TVC23000183 BXDGZ-23010空运联络单-巴西富士康-5.xlsx')
wb.columns = [0,1,2,3,4,5,6,7,8,9,10,11,12]
#wb[][5:20]
#print(wb[1][6:30])

wb.iloc['Part Number']

varialvel = 'Renan'

lista = [varialvel]

print(lista)