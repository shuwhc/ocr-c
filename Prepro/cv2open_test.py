import cv2
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
img_file = "Prepro\Data\img01.jpg"
img = cv2.imread(img_file)

#cv2.imshow("orginal image", img)
#cv2.waitKey(0)


#function - turn img to greyscale
#def grayscale(image): 
    #return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray_img = grayscale(img)
#cv2.imwrite("Prepro\SemiData\gray.jpg", gray_img)

##


originalImage = cv2.imread("Prepro\Data\img01.jpg")
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 
cv2.imshow('Black white image', blackAndWhiteImage)
#cv2.imshow('Original image',originalImage)
cv2.imshow('Gray image', grayImage)
  
cv2.waitKey(0)
cv2.destroyAllWindows()