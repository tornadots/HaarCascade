# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:10:11 2017

@author: trabz
"""



import numpy as np
import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread('C:\\Users\\trabz\\Desktop\\g1.jpg',0)          # queryImage
img2 = cv2.imread('C:\\Users\\trabz\\Desktop\\g3.jpg',0) # trainImage

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)


# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.9*n.distance:
        good.append([m])
# cv2.drawMatchesKnn expects list of lists as matches.
img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,img2,flags=2)
plt.imshow(img3),plt.show()
cv2.imwrite('deneme.jpg',img3)
