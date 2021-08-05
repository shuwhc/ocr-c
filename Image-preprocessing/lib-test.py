from PIL import Image

img01_file = "Image-preprocessing\Data\img01.jpg"
img01 = Image.open(img01_file)
print (img01)

#img01.show() #show the image


img01.save("Image-preprocessing\SemiData\img01_1.jpg")
