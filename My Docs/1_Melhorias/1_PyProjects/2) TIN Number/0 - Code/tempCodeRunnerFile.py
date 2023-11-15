import pandas as pd
import glob

# Caminho dos arquivos:
# excel_path = r'C:\Users\renanalmeida\Desktop\Invoices\TVC23000271-巴西富士康-空运补料-7.19香港散货.xlsx'
excel_path = r'C:\Users\renanalmeida\Desktop\Invoices\K\*xlsx'
excel_path_save = r'C:\Users\renanalmeida\Desktop\My Docs\1) Melhorias\1) Python Projects\2) TIN Number\2 - Results\TPLinkPN.xlsx'

# Para a criacao do index inicial das tabelas:
initial_index = []
final_index = []

# Armazenando o nome das planilhas:
sheet = []
b = 0
# Armazenando as planilhas:
all_data = pd.DataFrame()

# Code: leitura caminhos + selecao abas
for file_path in glob.glob(excel_path):
    # data_sheet_name = pd.ExcelFile(file_path).sheet_names
    data = pd.read_excel(file_path, header=0, sheet_name=0)
    print(file_path)
    # achar o index de cada excel
    for initial_index in data.itertuples(index=True):
        for final_index in data.itertuples(index=True):
            if 'Part Number' in initial_index and 'Total:' in final_index:
                break
            # for final_index in data.itertuples(index=True):
            #     i = 0
        initial_index = list(initial_index)
        final_index = list(final_index)
        initial_index = initial_index[0] + 1
        final_index = final_index[0]
        range_index = final_index - initial_index
        print(file_path)
        print(initial_index, final_index, range_index)
        data = pd.read_excel(file_path, header=initial_index)
        data.columns = data.columns.str.upper()
        data = data.loc[:range_index-1, ['PART NUMBER',
                                            'MANUFACTURER', 'COUNTRY OF ORIGIN']]
        all_data = pd.concat([all_data, data])
        print(all_data)