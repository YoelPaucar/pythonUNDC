#-*- coding:utf-8-*-
import cv2
import numpy as np
image_path1='ivvi_512x512_gray.jpg'
image_path2='ivvi_512x512_gray_ri.jpg'
image1=cv2.imread(image_path1)
image2=cv2.imread(image_path2)
#blur
k=5
blur=cv2.blur(image2,(k,k))

cv2.imshow('Original',image1)
cv2.imshow('Original con ruido',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
