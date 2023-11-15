import pandas as pd
# import os
import glob

# Caminho dos arquivos:
excel_path = r'T:\Renana\*csv'
excel_path_save = r'T:\Renana\Eric_Test5.xlsx'

# Armazenando as planilhas:
all_data = pd.DataFrame()

# Code: leitura caminhos + Compilar arquivos.
for file_path in glob.glob(excel_path):
    # print('CAMINHO ', file_path)
    data = pd.read_csv(file_path)
    all_data = pd.concat([all_data, data])
    # print(all_data)
    all_data.to_excel(excel_path_save, index=False)
