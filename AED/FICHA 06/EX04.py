"""
Create a function imageGradiente() that creates an image of (250, 250) pixels, in RGB
mode. The image should represent a smooth gradient from blue to red (no green):
"""

from PIL import Image

pathImages = "./images/"

width = 250
height = 250

def ImageGradiente():
    imageSize = (width, height)
    image1 = Image.new(size = imageSize, mode ="RGB")
    pixelMap = image1.load()
    for i in range(width):
        for j in range (height):
            r = i
            g = 0
            b = 255-i
            pixelMap[i,j] = (r,g,b)

    image1.show()

ImageGradiente()