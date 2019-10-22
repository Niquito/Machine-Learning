import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
dolar_data = pd.read_csv('CotizacionDolar.csv')

#dolar_data = dolar_data.sort_values(by='Fecha', ascending=True)
#by='col1', ascending=False
y = dolar_data.Vendedor
X = dolar_data.Fecha

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

#dolar_model = DecisionTreeRegressor()
#dolar_model.fit(train_X, train_y)

print(dolar_data.head())
plt.plot(X, y)
plt.show()