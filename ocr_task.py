# coding: utf-8
# https://github.com/baloon11/system-of-recognition
from PIL import Image
from pytesseract import *
img=Image.open("test.png")
img_crop=img.crop((70, 100, 200, 200))

width , height = img_crop.size

new_width  = 680
new_height = new_width * height / width 
new_height = 680
new_width  = new_height * width / height

img_crop.resize((new_width, new_width), Image.ANTIALIAS).save("tmp_pic.jpg")

numbers = Image.open("tmp_pic.jpg")
out_file= open('out.txt', 'a')
out_file.write(image_to_string(numbers))
out_file.close()
