#-*- coding:utf-8-*-
import cv2
import numpy as np
image_path1='ivvi_512x512_gray.jpg'
image_path2='ivvi_512x512_gray_ri.jpg'
image1=cv2.imread(image_path1)
image2=cv2.imread(image_path2)
#blur
k=15
bilateral=cv2.bilateralFilter(image2,k,80,80)

cv2.imshow('Original',image1)
cv2.imshow('bilateral',bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
