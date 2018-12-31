import cv2
import sys

# Load XML classifieres
cas_path = 'C:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml'
#eye_path = 'examples/haarcascade/haarcascade_eye.xml'
eye_path = 'C:/opencv/sources/data/haarcascades/haarcascade_eye.xml'
clasificador = cv2.CascadeClassifier(cas_path)

imagen=cv2.imread('fotos.jpg')

imagenCinza=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
facesDetectadas = clasificador.detectMultiScale(imagenCinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
print(len(facesDetectadas))
print(facesDetectadas)

for(x,y,l,a)in facesDetectadas:
    print(x,y,l,a)
    cv2.rectangle(imagen,(x,y),(x+l,y+a),(255,0,255),2)
cv2.imshow("faces encontradas",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()