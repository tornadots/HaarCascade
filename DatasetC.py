# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:09:56 2018

@author: trabz
"""
import numpy as np

import cv2
cam = cv2.VideoCapture(0)
s="71";
sampleNum=0
while(True):
    ret, img = cam.read()
    sampleNum=sampleNum+1
    cv2.imwrite("100tl/User."+s +'.'+ str(sampleNum) + ".jpg", img)
    cv2.imshow('frame',img) 
    if cv2.waitKey(300) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum>35:
        break
cam.release()
cv2.destroyAllWindows()
