"""
Do a similar function, but create 3 vertical stripes, of 80 pixels each. Save the image in the
images subfolder, with the name flag.jpg
"""

from PIL import Image
import random

pathImages = "./images/"

width = 240
height = 240

def ImageArt():
    imageSize = (width, height)
    image2 = Image.new(size = imageSize, mode ="RGB")
    pixelMap = image2.load()
    for i in range(width):
        for j in range (height):
            if i < 80:
                pixelMap[i,j] = (0,0,255)
            elif i > 160:
                pixelMap[i,j] = (255,0,0)
            else:
                pixelMap[i,j] = (255,255,255)
    image2.show()
    image2.save(pathImages + "flag.jpg")

ImageArt()