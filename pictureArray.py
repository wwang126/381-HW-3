import PIL
import numpy
from PIL import Image
im = Image.open("128Thresh.png")

f = open("Image.txt", "w")

for pixel in iter(im.getdata()):
    if pixel == 255:
        f.write("0 ,")
    else :
        f.write("1 ,")
f.close
