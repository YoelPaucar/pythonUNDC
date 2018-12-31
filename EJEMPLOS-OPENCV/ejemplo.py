#-*- coding:utf-8-*-
import cv2
import numpy as np
image_file='ivvi.jpg'
img =cv2.imread(image_file)

kernel=np.ones((3,3),np.float32)/9
dst=cv2.filter2D(src=img,ddepth=-1, kernel=kernel)

cv2.imshow('Original',img)
cv2.imshow('Filter',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
