import pandas as pd

dados_frutas ={"Maça":[30],'Banana':[20]}
frutas = pd.DataFrame(data=dados_frutas);
print(frutas);

dados_vendas={"Maça": [1000,5000], 'Banana': [700,2000]}
ano_vendas= {'Vendas de 2022', 'Vendas de 2023'}

vendas_frutas = pd.DataFrame(data=dados_vendas, index=list(ano_vendas))
print (vendas_frutas)

crimes = pd.read_csv("crimes.csv", header=0)
print(crimes.head())
print("----------------------------------------------------------------\n")
print(crimes.dtypes)
print("----------------------------------------------------------------\n")

coluna_espicifica = crimes['AREA NAME'] 
print(coluna_espicifica)
print("----------------------------------------------------------------\n")

valor_maximo = crimes['Crm Cd'].max()
print(valor_maximo)
print("----------------------------------------------------------------\n")

valor_determinado = crimes[crimes['Crm Cd'] == 330]
print(valor_determinado)   