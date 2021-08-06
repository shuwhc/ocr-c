# pip install --upgrade pip
# pip install matplotlib
# pip install numpy
#pip install pillow
# pip install opencv-python
#pip install imutils
# pip install imutils
#3.8.5 

import math
from scipy import ndimage

import imutils
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np


#cv2.imshow("orginal image", img)
#cv2.waitKey(0)


# #function - turn img to greyscale
# def grayscale(image): 
#     return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray_img = grayscale(img)
# cv2.imwrite("Prepro\SemiData\gray.jpg", gray_img)

# ##


originalImage = cv2.imread( 'Prepro\SemiData\img01_1.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 
#cv2.imshow('Black white image', blackAndWhiteImage)
#cv2.imshow('Original image',originalImage)
#cv2.imshow('Gray image', grayImage)
#inverted_bw = cv2.bitwise_not(blackAndWhiteImage)
#cv2.imwrite("Prepro\SemiData\gray.jpg", grayImage)



#cv2.imwrite("Prepro\SemiData\bw.jpg", blackAndWhiteImage)

def orientation_correction(img, save_image = False):
    # GrayScale Conversion for the Canny Algorithm  
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # Canny Algorithm for edge detection was developed by John F. Canny not Kennedy!! :)
    img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
    # Using Houghlines to detect lines
    lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)
    
    # Finding angle of lines in polar coordinates
    angles = []
    for x1, y1, x2, y2 in lines[0]:
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        angles.append(angle)
    
    # Getting the median angle
    median_angle = np.median(angles)
    
    # Rotating the image with this median angle
    img_rotated = ndimage.rotate(img, median_angle)
    
    if save_image:
        cv2.imwrite('Prepro\SemiData\img09.jpg', img_rotated)
    return img_rotated
#####################################################################################################

img_rotated = orientation_correction(grayImage)

cv2.imshow("", img_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()