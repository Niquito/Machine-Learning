import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Datasets-convertidos/statsAtaque.csv")
df = df.sort_values('Rem',ascending=False)

print(df.head())
print(df.columns)
print(df.Rem.describe())

df = df.head(20)

plt.plot(df.Rem, df.Nombre)
plt.show()