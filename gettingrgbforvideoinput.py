# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 21:12:51 2021

@author: gauri
"""

import cv2;
cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    BGR = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    cv2.imshow('frame1',frame)
    cv2.imshow('frame2',gray)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()