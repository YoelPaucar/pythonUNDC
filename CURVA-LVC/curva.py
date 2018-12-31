import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
#INTEGRANTES
#CONDORI PAUCAR YOEL ANDRES
#SANCHES CUADROS JOSE
#Para este caso tambien hemos utilizado la misma informacion que el de Linal
archivo = pd.read_excel('Libro1.xlsx')
VarInd = ['PRESION_ARTERIAL', 'PESO']
VarDep = ['DIAGNOSTICO']

ListaInd = archivo[VarInd]
ListaDep = archivo[VarDep]

Ind = np.r_[ListaInd]
Dep = np.r_[ListaDep].ravel()


Modelo = svm.SVC(kernel = 'rbf', C = 0.6, gamma = 0.1).fit(Ind, Dep)
talla_min, talla_max = Ind[:,0].min()-1, Ind[:,0].max()+1
peso_min, peso_max = Ind[:,1].min()-1, Ind[:,1].max()+1
h = (talla_max/talla_min)/100
xx, yy = np.meshgrid(np.arange(talla_min, talla_max, h), np.arange(peso_min, peso_max, h))

plt.subplot(1,1,1)

# creando las regiones de separacion
Z = Modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, cmap = plt.cm.Paired, alpha = 0.4)
plt.scatter(Ind[:,0], Ind[:,1], c = Dep, cmap = plt.cm.Paired)
plt.xlabel('Presion Arterial')
plt.ylabel('Peso')
plt.title('Personas')
plt.show()