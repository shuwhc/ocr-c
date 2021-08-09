import math
import imutils
import cv2
import numpy as np
from scipy import ndimage
from skimage.filters import threshold_local
from matplotlib import pyplot as plt
from PIL import Image

# Importing img
originalImage = cv2.imread('Prepro\prototype_0.5\img01.jpg')

#########
#########
def orientation_correction(img, save_image = False): 
    # GrayScale Conversion for the Canny Algorithm  
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
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
    
    return img_rotated
########
########


# Rotate
rotatImgage = orientation_correction(originalImage)
# Export
cv2.imwrite("Prepro/prototype_0.5/rotatImg.jpg",rotatImgage)

# tranf rotated img to gray, bw, inv bw
grayImage = cv2.cvtColor(rotatImgage, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
inverted_bw = cv2.bitwise_not(blackAndWhiteImage)

#######
#######
def bw_scanner(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    T = threshold_local(gray, 21, offset = 5, method = "gaussian")
    return (gray > T).astype("uint8") * 255
#######
#######

grayImage = cv2.cvtColor(grayImage, cv2.COLOR_GRAY2RGB)
blackAndWhiteImage = cv2.cvtColor(blackAndWhiteImage, cv2.COLOR_GRAY2RGB)

bwGray = bw_scanner(grayImage)
bwBw = bw_scanner(blackAndWhiteImage)

# Exporting image
cv2.imwrite("Prepro\prototype_0.5\gray.jpg", grayImage)
cv2.imwrite("Prepro/prototype_0.5/bw.jpg", blackAndWhiteImage)
cv2.imwrite("Prepro\prototype_0.5\invBw.jpg", inverted_bw)
cv2.imwrite("Prepro/prototype_0.5/bwGray.jpg", bwGray)
cv2.imwrite("Prepro/prototype_0.5/bwBw.jpg", bwBw)

##
##
def noise_removal(image):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)
##
##

no_noise = noise_removal(bwGray)
cv2.imwrite("Prepro/prototype_0.5/bwGrayNoise.jpg",no_noise)

##
##
def thick_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)
##
##

dilated_image = thick_font(no_noise)
cv2.imwrite("Prepro/prototype_0.5/thick.jpg", dilated_image)

#transfering post-processed img to text
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#print(pytesseract.get_languages(config=''))
#ocr_result = pytesseract.image_to_string(dilated_image, lang='chi_tra')
#print ("thick")
#print ("thick")
#print (ocr_result)

ocr_result = pytesseract.image_to_string(no_noise, lang='chi_tra')
print ("no_noise")
print ("no_noise")
print (ocr_result)

ocr_result = pytesseract.image_to_string(bwGray, lang='chi_tra')
print ("bwGray")
print ("bwGray")
print (ocr_result)
