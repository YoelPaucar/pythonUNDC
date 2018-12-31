# instalar desde cmd -> users/admin/appdata/local/programs/python/python37/scripts
import numpy as np #pip install numpy
import pandas as pd #pip install pandas
import matplotlib.pyplot as plt #pip install matplotlib
from sklearn import svm #pip install svm

archivo = pd.read_excel('Personas1.xlsx') #carga el archivo excel
VarInd = ['TALLA', 'PESO'] # variable independiente
VarDep = ['TIPO'] # variable dependiente

ListaInd = archivo[VarInd] # obtiene los datos en lista
ListaDep = archivo[VarDep] # obtiene los datos ista

Ind = np.r_[ListaInd] # convierte la lista en arreglo bidimensional
Dep = np.r_[ListaDep].ravel() # convierte la lista en arreglo unidimensional con ravel

# creando la maquina el modeo
Modelo = svm.SVC(kernel = 'linear').fit(Ind, Dep)

# creando el eje X e Y
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
plt.xlabel('Talla')
plt.ylabel('Peso')
plt.title('Personas')
plt.show()