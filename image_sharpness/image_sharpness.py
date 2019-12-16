from PIL import Image, ImageEnhance

#Sharness
img1 = Image.open('img1.jpg')
enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance(0).save('img1edit.jpg')


""" #notes:
0 = blurry
1= orginal img
2 = image with increase Sharpness
3 = img with increase sharpness
 """