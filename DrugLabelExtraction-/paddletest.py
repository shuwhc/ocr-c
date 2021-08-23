# GitHub repo installation of paddle
#!python -m pip install paddlepaddle-gpu==2.0.0 -i https://mirror.baidu.com/pypi/simple

# Install paddle OCR
#!pip install paddleocr

# Clone paddle OCR repo - get FONTS for visualization
#git clone https://github.com/PaddlePaddle/PaddleOCR

from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
#if FileNotFoundError: Could not find module xxx\xxx\Library\bin\geos_c.dll'
#   conda install shapely

from matplotlib import pyplot as plt # plot images
import cv2 #opencv
import os # folder directory navigationpip

#paddleocr -h  #show help info

#conda install paddlepaddle-gpu==2.1.2 cudatoolkit=11.2 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge
# Setup model
ocr_model = PaddleOCR(lang='en')

img_path = os.path.join('.', 'C:/IA/ocr-c/PreproAndTesseract/ImgCleaned/2018071060775_final.jpg')

# Run the ocr method on the ocr model
result = ocr_model.ocr(img_path)
#result

for res in result:
    print(res[1][0]) 
    
# Extracting detected components
boxes = [res[0] for res in result] # 
texts = [res[1][0] for res in result]
scores = [res[1][1] for res in result]

# Specifying font path for draw_ocr method
font_path = os.path.join('PaddleOCR', 'doc', 'fonts', 'C:/IA/DrugLabelExtraction-/PaddleOCR/doc/fonts/chinese_cht.ttf')

# Import our image - drug 1/2/3
# imports image—
img = cv2.imread(img_path) 

# reorders the color channels
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

# Visualize our image and detections
# resizing display area
plt.figure(figsize=(15,15))

# draw annotations on image

annotated = draw_ocr(img, boxes, texts, scores, font_path = font_path) 

# show the image using matplotlib
cv2.imshow("",annotated) 
cv2.waitKey(0)


#https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.2/doc/doc_en/multi_languages_en.md#Install
