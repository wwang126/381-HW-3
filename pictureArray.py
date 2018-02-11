import PIL
import numpy
from PIL import Image
im = Image.open("128Thresh210.png")

f = open("Image.txt", "w")
imgW = 128
x = 0
y = 128
for pixel in iter(im.getdata()):
    if(x == imgW):
        x = 0
        y -= 1
    if pixel == 0:
        f.write("dotPrinter " + str(x) +  "  " + str(y) + " ++ ")
    x += 1
f.close
