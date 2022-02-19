import os
from re import ASCII
from PIL import Image
import cv2
import sys

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']


def resize_gray_image(image, new_width = 50):
    width, height = image.size
    aspect_ratio = height/width
    new_height = int(aspect_ratio * new_width)
    resize_gray_image = image.resize((new_width, new_height)).convert('L')
    return resize_gray_image

def pix2chars(image):
    pixels = image.getdata()
    charaters = "".join([
        ASCII_CHARS[pixel//25] for pixel in pixels
    ])
    return charaters

def generate_frame(image, new_width = 50):
    new_image_data = pix2chars(resize_gray_image(image))
    total_pixels = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)]
    for index in range(0, total_pixels, new_width)
    ])
    sys.stdout.write(ascii_image)
    os.system('cls')


cap = cv2.VideoCapture("test.mp4")
while(True):
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    generate_frame(Image.fromarray(frame))
    cv2.waitKey(10)
