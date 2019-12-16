#import pillow module
from PIL import Image

#resize image files
img1 = Image.open('img1.jpg')
MAX_SIZE = (200,200)
img1.thumbnail(MAX_SIZE)
img1.save('img1small.jpg')