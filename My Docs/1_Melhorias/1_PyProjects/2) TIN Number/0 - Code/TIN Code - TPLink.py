import pandas as pd
import glob
import os
import time

tempo_inicial = time.time()

# Caminho dos arquivos:
excel_path = r'C:\Users\renan\OneDrive\Área de Trabalho\Python Files\0Invoices\*xlsx'
# excel_path = r'C:\Users\renanalmeida\Desktop\Invoices\INV-11230119425 X515MA EE IO KB LCM ME Others Oct Huaqin by Sea.xlsx'
excel_path_save = r'C:\Users\renan\OneDrive\Área de Trabalho\Python Files\0Invoices\Final1.xlsx'

# Para a criacao do index inicial das tabelas:
initial_index = []
final_index = []
invoice_num = []

# Armazenando o nome das planilhas:
files = glob.glob("*xlsx")
file_path = []

# Armazenando as planilhas:
all_data = pd.DataFrame()

# Code: leitura caminhos + selecao abas
for file_path in glob.glob(excel_path):
    # print('CAMINHO ',file_path)
    # data_sheet_name = pd.ExcelFile(file_path).sheet_names
    data = pd.read_excel(file_path, header=0)
    # print(data_sheet_name)
    for initial_index in data.itertuples(index=True):
        if 'Part Number' in initial_index:
            # print("ABCABC", file_path)
            for final_index in data.itertuples(index=True):
                if 'Total:' in final_index:
                    # for invoice_num in data.itertuples(index=True):
                    #     if "InvoiceNo.:" in invoice_num:
                    print(os.path.basename(excel_path))
                    # print(invoice_num == "InvoiceNo.:")

                    initial_index = initial_index[0] + 1
                    final_index = final_index[0]
                    range_index = final_index - initial_index
                    # print(type(final_index), type(
                    # final_index), type(range_index))
                    data = pd.read_excel(
                        file_path, header=initial_index)
                    print(data)
                    data.columns = data.columns.str.upper()
                    data = data.loc[:range_index-1, ['PART NUMBER',
                                                     'MANUFACTURER', 'COUNTRY OF ORIGIN', 'U/P(US$)']]
                    # name = os.path.basename(file_path)
                    # name = name.rfind("TCV",)
                    data["Invoice File"] = os.path.basename(file_path)
                    # print(os.path.basename(file_path))
                    # data = data.loc[:range_index-1,['PART NUMBER','ITEM']]
                    all_data = pd.concat([all_data, data])
                    all_data.to_excel(excel_path_save, index=False)

                    print(data)

tempo_final = time.time()

print(f"{tempo_final - tempo_inicial} segundos")
