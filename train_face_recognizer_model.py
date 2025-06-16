#!/usr/bin/env python3
# REF: https://steam.oxxostudio.tw/category/python/ai/ai-face-recognizer.html

import cv2
import numpy as np

# load face model
detector = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# load model training method
recog = cv2.face.LBPHFaceRecognizer_create()

# lists for face storage
faces = []
ids = []

# train Andy_Liu picture
for i in range(16):
    img = cv2.imread(f'data/pic/andy_liu/image copy {i}.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_np = np.array(gray,'uint8')
    face = detector.detectMultiScale(gray)
    for(x,y,w,h) in face:
        faces.append(img_np[y:y+h,x:x+w])
        ids.append(1)

# train Elephant_Dee picture
for i in range(16):
    img = cv2.imread(f'data/pic/elephant_dee/image copy {i}.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_np = np.array(gray,'uint8')
    face = detector.detectMultiScale(gray)
    for(x,y,w,h) in face:
        faces.append(img_np[y:y+h,x:x+w])
        ids.append(2)

# train myself picture
for i in range(16):
    img = cv2.imread(f'data/pic/myself/{i}.jpeg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_np = np.array(gray,'uint8')
    face = detector.detectMultiScale(gray)
    for(x,y,w,h) in face:
        faces.append(img_np[y:y+h,x:x+w])
        ids.append(3)

# start to train model
print('info: training model...')
recog.train(faces,np.array(ids))

# save face attribute to face.yml
recog.save('data/face.yml')
print('info: model training doen!')
