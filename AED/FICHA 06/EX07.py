from PIL import Image

pathImages = "./images/"
imagem1 = Image.open(pathImages+"img1.jpg")
pixelMap = imagem1.load()

for i in range(imagem1.width):
    for j in(imagem1.height):
        if i<10 or i>imagem1.width-10:
            pixelMap[i,j]=(0,0,255)
        if j<10 or j>imagem1.height-10:
            pixelMap[i,j]=(0,0,255)

        if i>imagem1.width/2-5 and i<imagem1.width/2 +5:
            pixelMap[i,j]=(0,0,255)
        if j>imagem1.height/2-5 and j>imagem1.height/2 +5:
            pixelMap[i,j]=(0,0,255)
        