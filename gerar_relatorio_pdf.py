import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_pdf import PdfPages
import plotly.express as px
import plotly.io as pio
import io

# Carregar dataset
df = pd.read_csv("Taxas_de_Rendimento_Escolar_2013_2023.csv")
df_em = df[df["Etapa_Ensino"] == "Ensino Médio"]
df_ano = df_em[df_em["Ano"] == 2022]

# Criar PDF
with PdfPages("Relatorio_Abandono_Escolar.pdf") as pdf:

    # Página de título
    plt.figure(figsize=(11.69, 8.27))
    plt.axis("off")
    plt.text(0.5, 0.6, "Relatório: Taxa de Abandono Escolar\nEnsino Médio (2013-2023)",
             fontsize=20, ha='center', va='center')
    plt.text(0.5, 0.4, "Base: INEP | Visualizações geradas em Python", fontsize=12, ha='center')
    pdf.savefig()
    plt.close()

    # Gráfico 1 - Linha temporal
    fig1 = px.line(df_em, x="Ano", y="Taxa_Abandono", color="Regiao",
                   title="Taxa de Abandono Escolar no Ensino Médio por Região (2013-2023)")
    img_bytes = pio.to_image(fig1, format='png')
    plt.figure(figsize=(11.69, 8.27))
    plt.imshow(plt.imread(io.BytesIO(img_bytes)))
    plt.axis('off')
    pdf.savefig()
    plt.close()

    # Gráfico 2 - Barras por região
    fig2 = px.bar(df_ano, x="Regiao", y="Taxa_Abandono", color="Regiao",
                  title="Taxa de Abandono Escolar por Região - 2022")
    img_bytes = pio.to_image(fig2, format='png')
    plt.figure(figsize=(11.69, 8.27))
    plt.imshow(plt.imread(io.BytesIO(img_bytes)))
    plt.axis('off')
    pdf.savefig()
    plt.close()

    # Gráfico 3 - Treemap
    fig3 = px.treemap(df_ano, path=["Regiao", "Unidade_Geografica", "Dependencia_Administrativa"],
                      values="Taxa_Abandono", title="Treemap - Região, Estado e Administração - 2022")
    img_bytes = pio.to_image(fig3, format='png')
    plt.figure(figsize=(11.69, 8.27))
    plt.imshow(plt.imread(io.BytesIO(img_bytes)))
    plt.axis('off')
    pdf.savefig()
    plt.close()

    # Gráfico 4 - Grafo
    estados = df_ano["Unidade_Geografica"].unique()
    G = nx.Graph()
    for i in range(len(estados)):
        for j in range(i + 1, len(estados)):
            media_i = df_ano[df_ano["Unidade_Geografica"] == estados[i]]["Taxa_Abandono"].mean()
            media_j = df_ano[df_ano["Unidade_Geografica"] == estados[j]]["Taxa_Abandono"].mean()
            if abs(media_i - media_j) < 0.5:
                G.add_edge(estados[i], estados[j])
    plt.figure(figsize=(12, 8))
    nx.draw_networkx(G, with_labels=True, node_color='lightblue', edge_color='gray',
                     node_size=2000, font_size=10)
    plt.title("Estados com Taxas de Abandono Semelhantes (Diferença < 0.5%)")
    pdf.savefig()
    plt.close()
