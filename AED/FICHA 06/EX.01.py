"""
Develop an ImageArt() function that creates an image of (400, 400) pixels, in RGB mode.
The function should fill the pixel map of the image with randomly generated RGB (Red,
Green, Blue). Each of them between 0 and 255.
Show the image and save it, with the name imageArt.jpg , to an image subfolder.
"""

from PIL import Image
import random

pathImages = "./images/"

width = 400
height = 400

def ImageArt():
    imageSize = (width, height)
    image1 = Image.new(size = imageSize, mode ="RGB")
    pixelMap = image1.load()
    for i in range(width):
        for j in range (height):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            pixelMap[i,j] = (r,g,b)
    
    image1.show()
    image1.save(pathImages + "imageArt.jpg")

ImageArt()

