from PIL import Image, ImageEnhance

# contrast
img1 = Image.open('img1.jpg')
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(0).save('img1edit.jpg')

""" #Notes :
0 = dark img 
1 = Orginal
2 = icrease contrast
3 = ........... """

