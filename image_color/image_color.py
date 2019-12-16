from PIL import Image, ImageEnhance

#color
img1 = Image.open('img1.jpg')
enhancer = ImageEnhance.Color(img1)
enhancer.enhance(0).save('img1edit.jpg')

""" #Notes :
0 = black in white 
1 = Orginal
2 = icrease color opacity
3 = ........... """