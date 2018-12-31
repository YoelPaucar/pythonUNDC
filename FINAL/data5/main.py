import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from sklearn import svm

archivo = pd.read_excel('Data5.xlsx')
encInd = ['Variable B','Variable A']
encDep = ['Variable C']

listaInd = archivo[encInd]
listaDep = archivo[encDep]

X = np.r_[listaInd]
Y = np.r_[listaDep].ravel()

valorAMinimo, valorAMaximo = X[:,0].min()-1, X[:,0].max()+1
valorBMinimo, valorBMaximo = X[:,1].min()-1, X[:,1].max()+1

h= (valorAMaximo/valorAMinimo)/100
rectax, rectay = np.meshgrid(np.arange(valorAMinimo,valorAMaximo,h),np.arange(valorBMinimo,valorBMaximo,h))

modelo = svm.SVC(kernel='linear').fit(X, Y)
z=modelo.predict(np.c_[rectax.ravel(), rectay.ravel()])
z=z.reshape(rectax.shape)

w = modelo.coef_[0]
a = -w[0] / w[1]

xx = np.linspace(10,valorBMaximo-valorBMinimo+15)+valorAMinimo-10
yy = a * xx - (modelo.intercept_[0]) / w[1]

b = modelo.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = modelo.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

plt.contourf(rectax,rectay,z, cmap = plt.cm.Paired, alpha = 0.3)
plt.scatter(modelo.support_vectors_[:, 0], modelo.support_vectors_[:, 1],cmap = plt.cm.Paired, alpha = 0.3)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)

plt.plot(xx, yy)
plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k--')

plt.xlabel("A")
plt.ylabel("B")
plt.title("Data 5")
plt.subplot(1, 1, 1)
plt.show()


