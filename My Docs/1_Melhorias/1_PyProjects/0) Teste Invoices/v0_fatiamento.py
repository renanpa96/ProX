import os
import pandas as pd
import glob


file_location = r'Q:\FBR-MAO\Purchasing\Compras FBRLA\INVOICES IMPORTADOS\TP-LINK\2. Invoices\Pasta de Invoices\05.23\final invoices--5.3\final invoices--5.3\TVC23000171 EX220-巴西富士康-5.3.xlsx'
# index_location = final_index - initial_idex
# excel_files = glob.glob(location)

db1 = pd.read_excel(file_location, sheet_name=0)

# #testando com o iloc
# initial_idex_iloc = db1[db1.iloc[:,[0]] == "Item"]
# print(initial_idex_iloc.head(40))

# testando sem o iloc
initial_idex = db1.index[db1["TP-Link Lianzhou Co., Ltd."] == "Item"]
# initial_idex = db1[db1["TP-Link Lianzhou Co., Ltd."] == "Item"]
# print(initial_idex)

print(initial_idex)

dezoito = 18

db = pd.read_excel(file_location, sheet_name=0, usecols=[0], skiprows=dezoito)


print(db)
print(db.tail(30))
# fatiando uma parte
print(db)

db1 = db[db["TP-Link Lianzhou Co., Ltd."] >= 1]

print(db1)
