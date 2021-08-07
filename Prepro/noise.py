
import pytesseract
from PIL import Image
import cv2

from pytesseract import Output


img_file = "Prepro\SemiData\gray.jpg"
img = cv2.imread(img_file)


result = cv2.medianBlur(img,3)

cv2.imwrite("Prepro\SemiData\Bw-noNoise.jpg",result)
cv2.imshow("",result)
cv2.waitKey(0)
cv2.destroyAllWindows()