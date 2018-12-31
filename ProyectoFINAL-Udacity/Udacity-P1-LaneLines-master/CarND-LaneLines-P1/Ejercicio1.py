import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
import cv2
#%matplotlib inline
from moviepy.editor import VideoFileClip
from IPython.display import HTML

imageDir = 'test_images/'
imageFiles = os.listdir(imageDir)

imageList = []

for i in range(0, len(imageFiles)):
    imageList.append(mpimg.imread(imageDir + imageFiles[i]))

print(imageFiles)

def display_images(images, cmap=None):
    plt.figure(figsize=(40, 40))
    for i, image in enumerate(images):
        plt.subplot(3, 2, i + 1)
        plt.imshow(image, cmap)
        plt.autoscale(tight=True)
    plt.show()


display_images(imageList)


def color_filter(image):
    # convert to HLS to mask based on HLS
    hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
    lower = np.array([0, 190, 0])
    upper = np.array([255, 255, 255])

    yellower = np.array([10, 0, 90])
    yelupper = np.array([50, 255, 255])

    yellowmask = cv2.inRange(hls, yellower, yelupper)
    whitemask = cv2.inRange(hls, lower, upper)

    mask = cv2.bitwise_or(yellowmask, whitemask)
    masked = cv2.bitwise_and(image, image, mask=mask)

    return masked


filtered_img = list(map(color_filter, imageList))

display_images(filtered_img)


