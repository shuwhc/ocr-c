from PIL import Image

img01_file = "Prepro\Data\img01.jpg"
img01 = Image.open(img01_file)
print (img01)

#img01.show() #show the image


img01.save("Prepro\SemiData\img01_1.jpg")
