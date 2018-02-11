import PIL
import numpy
from PIL import Image
im = Image.open("200Thresh215.png")

f = open("Image.txt", "w")
imgW = 400
x = 0
y = 400
for pixel in iter(im.getdata()):
    if(x == imgW):
        x = 0
        y -= 2
    if pixel == 0:
        f.write("dotPrinter " + str(x) +  "  " + str(y) + " ++ ")
    x += 2
f.close
