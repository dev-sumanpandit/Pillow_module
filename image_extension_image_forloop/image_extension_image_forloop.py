#import pillow module and os module
from PIL import Image
import os

#changing extension of  multiple images using for loop
for item in os.listdir():
    if item.endswith('.jpg'):
        img1 = Image.open(item)
        filename,extension = os.path.splitext(item)
        img1.save(f'{filename}.png')

