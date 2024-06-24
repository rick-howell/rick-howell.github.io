# This file will take png images and convert them to webp format for faster loading times on the web.

from PIL import Image
import os

IMAGE_PATH = 'img/'

# We'll take every png image in the img folder and convert it to webp format


for file in os.listdir(IMAGE_PATH):
    if file.endswith('.png'):
        img = Image.open(IMAGE_PATH + file)
        img.save(IMAGE_PATH + file.replace('.png', '.webp'), 'webp')
        print(f'{file} converted to webp')


print('All images converted to webp format')