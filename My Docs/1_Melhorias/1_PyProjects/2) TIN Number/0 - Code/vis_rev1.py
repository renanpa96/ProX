import pandas as pd
import glob

# Caminho dos arquivos:
excel_path = r'C:\Users\renanalmeida\Desktop\Invoices\*xlsx'
# excel_path = r'C:\Users\renanalmeida\Desktop\Invoices\INV-11230119425 X515MA EE IO KB LCM ME Others Oct Huaqin by Sea.xlsx'
excel_path_save = r'C:\Users\renanalmeida\Desktop\My Docs\1) Melhorias\1) Python Projects\2) TIN Number\2 - Results\Final1.xlsx'

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
    # print('CAMINHO ',file_path)
    data_sheet_name = pd.ExcelFile(file_path).sheet_names
    # print(data_sheet_name)
    for sheet in data_sheet_name:
        if 'C' in sheet:
            data = pd.read_excel(file_path, header=0,)
            # print(data)
            # achar o index de cada excel
            for initial_index in data.itertuples(index=True):
                # print(initial_index)
                # print(initial_index[0])
                if 'Company' in initial_index:
                    break
            # index_usado = tuple(initial_index)
            # index_usado = index_usado[0]
            # initial_index = index_usado + 1
            # Initial_index inicialmente e uma tupla, com o parentesis zero a gente tem o valor como inteiro, por alguma razao a planilha nao comecao com Asustek e por isso eu somo um em cada laco do looping
            initial_index = initial_index[0] + 1
            # print('apos o if o initial index e ', initial_index)
            # achar o index final
            for final_index in data.itertuples(index=True):
                # print(final_index)
                if 'TOTAL: ' in final_index:
                    # index_usado = tuple(final_index)
                    # index_usado = index_usado[0]
                    # # print(index_usado)
                    # # print(type(index_usado))
                    # index_usado = index_usado-1
                    # print(index_usado)
                    break
            final_index = final_index[0]
            # depois do for, usar os indices max e min
            range_index = final_index - initial_index
            # print(initial_index, final_index, range_index)
            # print(i)
            data = pd.read_excel(file_path, header=initial_index)
            # para deixar as colunas com letra maiuscula
            data.columns = data.columns.str.upper()
            print(data.columns)
            print(file_path)
            # b = b + 1
            # print(file_path, b)
            try:
                data = data.loc[:range_index-1, ['COMPANY',
                                                 'COUNTRY', 'ADDRESS', 'TIN CODE', 'SISFAC']]
            except KeyError:
                # print ('entrou no except: ', file_path)
                # print('Except 1: ', file_path, ' sheet > ', sheet)
                # print(file_path)
                data = data.loc[:range_index-1, ['COMPANY',
                                                 'COUNTRY', 'ADDRESS', 'TIN NUMBER', 'SISFAC']]
            # except
            #       data = data.loc[:range_index-1, ['Company', 'Address', 'SISFAC']]
            #       print(file_path)
            # except:
            #     print('Except 2: ', file_path, ' sheet > ', sheet)
            #     data = data.loc[:range_index-1, ['Company', 'Country', 'Address', 'TIN Number']]
            #     print(data)
            #     pass

            all_data = pd.concat([all_data, data])
            all_data.to_excel(excel_path_save)

            # print (data.columns)
            # print(list(data.columns))

            # data = data.iloc[]
            # data = pd.read_excel(i,usecols=['TIN Code','SISFAC','Company'])
            # print(data)
            # print(initial_index[0])
            # print(final_index[0])
            # data_sliced = data.drop(index=)
