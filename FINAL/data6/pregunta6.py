import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from sklearn import svm

archivo = pd.read_excel('Data6.xlsx')
encInd = ['variable_a','variable_b']
encDep = ['variable_c']

listaInd = archivo[encInd]
listaDep = archivo[encDep]

varInd = np.r_[listaInd]
varDep = np.r_[listaDep].ravel()

tallaMinima, tallaMaxima = varInd[:,0].min()-2,varInd[:,0].max()+1
pesoMinimo, pesoMaximo = varInd[:,1].min()-2,varInd[:,1].max()+1
h = (tallaMaxima+1/tallaMinima+1)/100
rectax, rectay = np.meshgrid(np.arange(tallaMinima,tallaMaxima,h),np.arange(pesoMinimo,pesoMaximo,h))

modelo = svm.SVC(kernel='linear').fit(varInd,varDep)
z=modelo.predict(np.c_[rectax.ravel(), rectay.ravel()])
z=z.reshape(rectax.shape)

plt.contourf(rectax,rectay,z,cmap = plt.cm.Paired,alpha = 0.4)
plt.scatter(varInd[:,0],varInd[:,1], c = varDep, cmap = plt.cm.Paired)

plt.xlabel("A")
plt.ylabel("B")
plt.title("Data 6")
plt.subplot(1,1,1)
plt.show()
