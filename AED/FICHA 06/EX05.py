"""
Create an imageFrame() function that takes an image as the input argument, and creates
a frame around it with 20 pixels in magenta, as illustrated below.
"""

from PIL import Image

pathImages = ".\\images\\"
imagem1 = Image.open(pathImages+"img1.jpg")
pixelMap = imagem1.load()

def imageFrame():

    for i in range(imagem1.width):
        for j in range (imagem1.height):
            if j < 20 or j > imagem1.height-20:
                pixelMap[i,j] = (255,0,255)
            if i < 20 or i > imagem1.width-20:
                pixelMap[i,j] = (255,0,255)

    imagem1.show()
    imagem1.save(pathImages+"img1Moldura.jpg")
        
imageFrame()