import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("snic-provincias.csv")

print(df.head())
print(df.columns)
print(df.anio.describe())
plt.plot(df.anio, df.cantidad_hechos)
plt.show()