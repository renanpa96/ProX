import os
import pandas as pd
import glob


location = r'Q:\FBR-MAO\Purchasing\Compras FBRLA\INVOICES IMPORTADOS\TP-LINK\2. Invoices\Pasta de Invoices\05.23\final invoices--5.3\final invoices--5.3\*.xlsx'

excel_files = glob.glob(location)

# print(excel_files)

# Atribuir uma var vazia para colocar a compilacao das variaveis
df1_concat = pd.DataFrame()


for excel_file in excel_files:
    df_raw = pd.read_excel(excel_file, sheet_name=0)
    # df_raw1=df_raw[0]
    # print(df_raw1)
    # df_correction = df_raw[df_raw[0]!=0]
    df1_concat = pd.concat([df1_concat, df_raw])

df1_concat.to_excel(r'C:\Users\renanalmeida\Desktop\My Docs\df1.xlsx')
print(df1_concat)


# Daq pra baixo sao testes

# O que eu tinha feito

# caminho para os arquivos
path_date_base = pd.ExcelFile(
    r'Q:\FBR-MAO\Purchasing\Compras FBRLA\INVOICES IMPORTADOS\TP-LINK\2. Invoices\Pasta de Invoices\05.23\final invoices--5.3\final invoices--5.3\*.xlsx')


path_new_workbook = r'C:\Users\renanalmeida\Desktop\My Docs'

# manuseio da planilha > posso denominar a funcao como se fosse uma acao (metodo)
data_base_raw = pd.read_excel(path_date_base, sheet_name=0, usecols='A:J')
new_workbook = data_base_raw

# data_base_row.loc[data_base_row[0] > 1]
print(data_base_raw.head(40))

# separando os Part


# para criar uma Base comum, devemos colocar a func DataFrame
# master_date_base = pd.DataFrame()

# para printar os nomes das colunas
# column_names = data_base_row.columns.values
# print((column_names))
