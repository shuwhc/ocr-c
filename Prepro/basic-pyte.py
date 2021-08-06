import pytesseract
from PIL import Image
import cv2


img_file = 'Prepro\SemiData\gray.jpg'
img = cv2.imread(img_file)

#cv2.imshow('abc',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
ocr_result = pytesseract.image_to_string(img)
print (ocr_result)


