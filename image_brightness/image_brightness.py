from PIL import Image, ImageEnhance
#Brightness
img1 = Image.open('img1.jpg')
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(0).save('img1edit.jpgls')

""" #Notes :
0 = dark 
1 = Orginal
2 = Brighter Image
3 = ........... """