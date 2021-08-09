from PIL import Image
import pytesseract
from pytesseract import Output
import cv2
import numpy as np
from matplotlib import pyplot as plt
import re



img1 = cv2.imread("Prepro/prototype_0.5/bwGrayNoise.jpg")
#img1 = cv2.imread('D:/School/School_sem3/IA/IA_project/test_3.jpg')
new2 = cv2.resize(img1 ,(600,800),interpolation= cv2.INTER_CUBIC)
d = pytesseract.image_to_data(new2, output_type=Output.DICT, lang="eng")
#d = pytesseract.image_to_boxes(new2)
keys = list(d.keys())
date_pattern = "[0-9]"
date_pattern2 = '[a-zA-Z0-9]'
print(d.keys())

n_boxes = len(d['text'])
for i in range(n_boxes):
    if float(d['conf'][i]) > 60:
        if re.match(date_pattern2, d['text'][i]):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            cv2.rectangle(new2, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('output', new2)
cv2.waitKey(0)