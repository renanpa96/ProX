import pandas as pd

location = r'Q:\FBR-MAO\Purchasing\Compras FBRLA\INVOICES IMPORTADOS\TP-LINK\2. Invoices\Pasta de Invoices\05.23\final invoices--5.3\final invoices--5.3\TVC23000171 EX220-巴西富士康-5.3.xlsx'

db = pd.read_excel(location)
# No iloc e a seguinte estrutura para rows e col
# d.iloc[linhas , [coluna]] > apenas numeros

# para retornar uma serie de valores
# d.iloc[ linhas_comeco : linha_fim , [coluna_comeco : coluna_fim]]

# a parte da coluna dessa forma [,[]] > db.iloc[linha,[coluna]]
# traz a base inteira dentro impressa, mas expoe apenas os campos com a igualdade
#db = db[db.iloc[:,[0]] =='Item'] 

# a coluna dessa forma [,] > db.iloc[linha,coluna]
# traz a linha inteira que contem os valores, mas nao a base toda
#db = db[db.iloc[:,0] =='Item'] 


db_index_item = db[db.iloc[:,0] =='Item']

db_index_item = db_index_item.index

# tem diferenca entre last_valid_index() e last_valid_index
# o primeiro imprime tudo ate o ultimo index valido
# o segundo imprime apenas o valor escalar do Index (val do Index)
db = db.last_valid_index()
print(db)