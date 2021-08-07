from skimage.filters import threshold_local
import math
from scipy import ndimage

import imutils
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

def bw_scanner(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    T = threshold_local(gray, 21, offset = 5, method = "gaussian")
    return (gray > T).astype("uint8") * 255



img_file = "Prepro\SemiData\gray.jpg"
img = cv2.imread(img_file)


result = bw_scanner(img)

cv2.imwrite("Prepro\SemiData\Bw.jpg",result)
cv2.imshow("",result)
cv2.waitKey(0)
cv2.destroyAllWindows()