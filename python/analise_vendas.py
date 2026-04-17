import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/vendas.csv")

print("Resumo dos dados:")
print(df.describe())

vendas_categoria = df.groupby("categoria")["valor"].sum()

print(vendas_categoria)

vendas_categoria.plot(kind="bar")

plt.title("Vendas por Categoria")
plt.ylabel("Total de vendas")

plt.show()
