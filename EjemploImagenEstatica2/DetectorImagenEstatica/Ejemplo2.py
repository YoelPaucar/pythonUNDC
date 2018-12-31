import cv2
image = cv2.imread('bikel.jpg',cv2.IMREAD_GRAYSCALE)

k=3
sobelx = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=k)
sobely = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=k)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow('Original', image)
cv2.namedWindow("Sobel X", cv2.WINDOW_NORMAL)
cv2.imshow('Sobel X', sobelx)
cv2.namedWindow("Sobel Y", cv2.WINDOW_NORMAL)
cv2.imshow('Sobel Y', sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()