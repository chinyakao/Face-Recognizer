#!/usr/bin/env python3
# REF: https://steam.oxxostudio.tw/category/python/ai/opencv-read-image.html

import cv2

img_1 = cv2.imread('data/catmeme.png')

# use different color mode to open image
img_2 = cv2.imread('data/catmeme.png', cv2.IMREAD_GRAYSCALE)

# use '2' in grayscale mode
img_3 = cv2.imread('data/catmeme.png', 2) 

try:
    cv2.imshow('studio_1',img_1)
    cv2.imshow('studio_2',img_2)
    cv2.imshow('studio_3',img_3)

    # click any key to close image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print('Picture not found')