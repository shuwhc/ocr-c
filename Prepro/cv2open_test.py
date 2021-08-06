# pip install --upgrade pip
# pip install matplotlib
# pip install numpy
#pip install pillow
# pip install opencv-python
#pip install imutils

#3.8.5 

import  imutils
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
img_file = 'Prepro\Data\img06.jpg'
img = cv2.imread(img_file)

#cv2.imshow("orginal image", img)
#cv2.waitKey(0)


# #function - turn img to greyscale
# def grayscale(image): 
#     return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray_img = grayscale(img)
# cv2.imwrite("Prepro\SemiData\gray.jpg", gray_img)

# ##


originalImage = cv2.imread( 'Prepro\Data\img06.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 
#cv2.imshow('Black white image', blackAndWhiteImage)
#cv2.imshow('Original image',originalImage)
cv2.imshow('Gray image', grayImage)

#inverted_bw = cv2.bitwise_not(blackAndWhiteImage)
#cv2.imshow('Inv image', inverted_bw)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


#cv2.imwrite("Prepro\SemiData\bw.jpg", blackAndWhiteImage)
#cv2.imwrite("Prepro\SemiData\gray.jpg", grayImage)



###############################################





