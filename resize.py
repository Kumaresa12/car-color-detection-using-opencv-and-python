import cv2

img=cv2.imread('car-image.jpg')

imgResize=cv2.resize(img,(300,200))
cv2.imwrite('resized-image.jpg',imgResize)
cv2.imshow('Original',img)
cv2.imshow('Resized',imgResize)

cv2.waitKey(0)