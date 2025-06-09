import pandas as pd
import plotly.express as px

# Carregar o dataset
df = pd.read_csv('dataset/Taxas_de_Rendimento_Escolar_2013_2023.csv')

# Filtrar apenas os anos de 2022 e 2023
df_filtered = df[df['Ano'].isin([2022, 2023])]

# Criar um gráfico interativo
fig = px.line(df_filtered, x="Ano", y="Taxa de Abandono", color="Região", title="Evolução do Abandono Escolar por Região")
fig.show()
