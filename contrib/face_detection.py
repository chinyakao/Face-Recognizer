#!/usr/bin/env python3
# REF: https://steam.oxxostudio.tw/category/python/ai/ai-face-dectection.html#a1

import cv2

"""
Detect a face in a picture
"""
# load image source and turn image to gray scale (suggested)
img = cv2.imread('data/mona.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# load face model
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# facical detection
faces = face_cascade.detectMultiScale(gray)

# for loop to catch face attribution in a square
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('studio', img)

# press any key to stop
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Detect a face in live video
"""
# laod live video by camera
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
if not cap.isOpened(): 
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    # resize for better performance
    frame = cv2.resize(frame,(480,320))

    # turn camera video to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # face detection
    faces = face_cascade.detectMultiScale(gray)
    
    # label face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('live_video_studio', frame)

    # press 'q' to stop
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()