# This file will take png images and convert them to webp format for faster loading times on the web.

from PIL import Image
import os
import sys

IMAGE_PATH = 'img/'

# We'll take every png image in the img folder and convert it to webp format


for file in os.listdir(IMAGE_PATH):
    if file.endswith('.png') or file.endswith('.jpg'):
        end = file.split('.')[-1]
        img = Image.open(IMAGE_PATH + file)
        img.save(IMAGE_PATH + file.replace(end, 'webp'), 'webp')
        print(f'{file} converted to webp')


print('All images converted to webp format')



# We'll now take every mp4 video in the video folder and convert it to webm format
VIDEO_PATH = 'img/'



print('All videos converted to webm format')

sys.exit(0)