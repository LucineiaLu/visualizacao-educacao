import pandas as pd

# Carregando o dataset
df = pd.read_csv("Taxas_de_Rendimento_Escolar_2013_2023.csv")

# Exibindo as colunas disponíveis
print(df.columns)

# Exibindo as primeiras linhas
print(df.head())
