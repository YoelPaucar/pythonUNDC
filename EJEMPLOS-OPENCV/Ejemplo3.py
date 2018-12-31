#-*- coding:utf-8-*-
import cv2
import numpy as np
image_path1='ivvi_512x512_gray.jpg'
image_path2='ivvi_512x512_gray_ri.jpg'
image1=cv2.imread(image_path1)
image2=cv2.imread(image_path2)
#blur
k=5
sigma=0
blur=cv2.GaussianBlur(image2,(k,k),sigma)

cv2.imshow('Original',image1)
cv2.imshow('Gaussian',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
