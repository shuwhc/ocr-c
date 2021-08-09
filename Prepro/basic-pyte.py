import pytesseract
from PIL import Image
import cv2

from pytesseract import Output
img_file = "Prepro\SemiData\BW.jpg"
img = cv2.imread(img_file)


#cv2.imshow('',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#print(pytesseract.get_languages(config=''))
ocr_result = pytesseract.image_to_string(img, lang="chi_tra")
print (ocr_result)