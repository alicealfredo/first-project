"""
Look for the example available in Moodle (PILLOW presentation) that creates an image
(240, 240) with 3 stripes each of them 80 pixels high (blue, white, red).
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
            if j < 80:
                pixelMap[i,j] = (0,0,255)
            elif j > 160:
                pixelMap[i,j] = (255,0,0)
            else:
                pixelMap[i,j] = (255,255,255)
    image2.show()

ImageArt()