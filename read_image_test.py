import cv2
# img = cv2.imread('catmeme.png')

# use different color mode to open image
# REF: https://steam.oxxostudio.tw/category/python/ai/opencv-read-image.html
# use cv2.IMREAD_GRAYSCALE mode
img = cv2.imread('catmeme.png', cv2.IMREAD_GRAYSCALE)
# use '2' in grayscale mode
# img = cv2.imread('catmeme.png', 2) 

try:
    cv2.imshow('studio',img)
    cv2.waitKey(0) # click any key to close image
    cv2.destroyAllWindows()
except:
    print('Picture not found')