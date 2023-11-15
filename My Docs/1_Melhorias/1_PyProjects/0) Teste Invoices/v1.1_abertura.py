import pandas as pd
import glob
import win32

location = r'Q:\FBR-MAO\Purchasing\Compras FBRLA\INVOICES IMPORTADOS\TP-LINK\2. Invoices\Pasta de Invoices\05.23\final invoices--5.10\final invoices--5.10\*.xlsx'

excel_files = glob.glob(location)

print(excel_files)

# Atribuir uma var vazia para colocar a compilacao das variaveis
df1_concat = pd.DataFrame()

file_name = ""

for excel_file in excel_files:
    file_name = excel_file.partition()
    print(file_name)
    df_raw = pd.read_excel(excel_file, sheet_name=0)
    # df_raw1=df_raw[0]
    # print(df_raw1)
    # df_correction = df_raw[df_raw[0]!=0]
    df1_concat = pd.concat([df1_concat, df_raw])

df1_concat.to_excel(r'C:\Users\renanalmeida\Desktop\My Docs\df1.xlsx')
print(df1_concat)


# Daq pra baixo sao testes
