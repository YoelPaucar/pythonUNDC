#-*- coding:utf-8-*-
import cv2
import numpy as np
image_path1='ivvi_512x512_gray.jpg'
image_path2='ivvi_512x512_gray_ri.jpg'
image1=cv2.imread(image_path1)
image2=cv2.imread(image_path2)
#blur
k=5
medianblur=cv2.medianBlur(image2,k)

cv2.imshow('Original',image1)
cv2.imshow('Median',medianblur)
cv2.waitKey(0)
cv2.destroyAllWindows()
