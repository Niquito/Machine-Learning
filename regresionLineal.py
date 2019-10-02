import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

precioCasas = [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]
tamaño = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]

tamaño2 = np.array(tamaño).reshape((-1, 1))

regr = linear_model.LinearRegression()
regr.fit(tamaño2, precioCasas)

print("Coeficiente: \n", regr.coef_)
print("Intercepción: \n", regr.intercept_)

def grafico(form, x_rango):
	x = np.array(x_rango)
	y = eval(form)
	plt.plot(x, y)

grafico('regr.coef_*x + regr.intercept_', range(1000, 2700))
plt.scatter (tamaño, precioCasas, color="black")
plt.ylabel("Precios de casas")
plt.xlabel("Tamaño de casas")
plt.show()


#src https://www.slideshare.net/Simplilearn/machine-learning-with-python-machine-learning-algorithms-machine-learning-tutorial-simplilearn
