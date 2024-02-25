import cv2 as cv
import numpy as np

# Read an image
image1 = cv.imread(r'\opencv\photos\cats.jpg')


# Display the original image
cv.imshow('Original Image', image1)

# Resize the image
resized_image = cv.resize(image1, (500, 200))
cv.imshow('Resized Image', resized_image)

#  grayscale
gray_image = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray_image)

#  Gaussian blur to the grayscale image
blurred_image = cv.GaussianBlur(gray_image, (5, 5), 0)
cv.imshow('Blurred Image', blurred_image)

# Draw a rectangle on the original image
cv.rectangle(image1, (50, 50), (200, 150), (0, 255, 0), thickness=2)
cv.imshow('Rectangle on Original Image', image1)

#cascade example
canny=cv.Canny(image1,200,300)
cv.imshow('edge cascade',canny)

#BGR to HSV
hsv=cv.cvtColor(image1,cv.COLOR_BGR2HSV)
cv.imshow('bgr>hsv',hsv)

#averaging
avrg=cv.blur(image1,(3,3))
cv.imshow('averaging',avrg)

#Laplacian
laplacian=cv.Laplacian(gray_image,cv.CV_64F)
laplacian=np.uint8(np.absolute(laplacian))
cv.imshow('laplacian',laplacian)

cv.waitKey(0)
cv.destroyAllWindows()
