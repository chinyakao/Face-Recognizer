#!/usr/bin/env python3
# REF: https://steam.oxxostudio.tw/category/python/ai/ai-face-recognizer.html

import cv2

# load face model, training data, method
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('data/face.yml')
cascade_path = 'data/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# open camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break

    # resize image for better performance
    img = cv2.resize(img, (270,200))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    # dict for face id & name
    name = {
        '1':'Andy Liu',
        '2':'Elephant Dee',
        '3':'Riley'
    }

    # recognize the 'face' and 'name'
    for(x,y,w,h) in faces:
        # detect and draw square
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        # predict the face id and confidence level
        idnum,confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
        # if the confidence level less than 60, then match the 'name'
        if confidence < 60:
            text = name[str(idnum)]
        else:
            text = 'Unknow'

        # put the 'name' above the square
        cv2.putText(img, text, (x,y-5),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)

    cv2.imshow('recognizer', img)

    # press 'q' to stop
    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()