import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv("C:/data_base/comparacao_contingencias.csv")

# Corrigir o formato dos valores analisados
df["Valor analisado"] = df["Valor analisado"].apply(lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

if "Valor analisado atualizado" in df.columns:
    df["Valor analisado atualizado"] = df["Valor analisado atualizado"].apply(lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Configurar estilo do gráfico para tema escuro e vibrante
plt.style.use("dark_background")

# Criar dashboard interativo com múltiplos gráficos
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Gráfico 1 - Distribuição de Risco
sns.countplot(data=df, x="#Risco", palette="coolwarm", ax=axes[0, 0])
axes[0, 0].set_title("Distribuição de Risco", fontsize=14)
axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=45)

# Gráfico 2 - Distribuição de Categorias
sns.countplot(data=df, x="#Categoria", palette="magma", ax=axes[0, 1])
axes[0, 1].set_title("Distribuição de Categorias", fontsize=14)
axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=45)

# Gráfico 3 - Distribuição de Polos
sns.countplot(data=df, x="Polo", palette="viridis", ax=axes[0, 2])
axes[0, 2].set_title("Distribuição de Polos", fontsize=14)

# Gráfico 4 - Top 10 Clientes por Frequência
top_clientes = df["#Clientes"].value_counts().nlargest(10)
sns.barplot(x=top_clientes.values, y=top_clientes.index, palette="Blues", ax=axes[1, 0])
axes[1, 0].set_title("Top 10 Clientes", fontsize=14)

# Gráfico 5 - Comparação de Valor Analisado entre Períodos
sns.boxplot(data=df, x="Período", y="Valor analisado", palette="cool", ax=axes[1, 1])
axes[1, 1].set_title("Valor Analisado - 12/2024 vs 01/2025", fontsize=14)

# Gráfico 6 - Comparação de Valor Analisado Atualizado (se disponível)
if "Valor analisado atualizado" in df.columns:
    sns.boxplot(data=df, x="Período", y="Valor analisado atualizado", palette="cool", ax=axes[1, 2])
    axes[1, 2].set_title("Valor Analisado Atualizado - 12/2024 vs 01/2025", fontsize=14)
else:
    # Gráfico 7 - Distribuição de Valores Analisados por Cliente
    sns.boxplot(data=df, x="#Clientes", y="Valor analisado", palette="Set3", ax=axes[1, 2])
    axes[1, 2].set_title("Distribuição de Valores Analisados por Cliente", fontsize=14)
    axes[1, 2].set_xticklabels(axes[1, 2].get_xticklabels(), rotation=45)

# Ajustar layout
plt.tight_layout()
plt.show()
