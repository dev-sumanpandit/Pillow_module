# Image blur ,Gaussian blur

from PIL import Image, ImageEnhance, ImageFilter
img1 = Image.open('img1.jpg')
img1.filter(ImageFilter.GaussianBlur()).save('img1edited.jpg')