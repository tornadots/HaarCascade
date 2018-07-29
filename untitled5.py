# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:05:21 2018

@author: trabz
"""

import cv2
import numpy as np
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('trainer/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<80):
         if(Id==1):
          Id2="Abdullah"
         elif(Id==5):
          Id2="Muhammed"
        elif(conf>=80):
         Id2="Saptanamadi"   
        cv2.putText(im, Id2, (x,y+h), font, 1, (0, 255, 0))
    cv2.imshow('im',im) 
    if cv2.waitKey(10) ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

