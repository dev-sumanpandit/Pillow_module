from PIL import Image

#change the image extension
img1 = Image.open('img1.jpg')
img1.save('img1.png')
img1.save('img1.pdf')