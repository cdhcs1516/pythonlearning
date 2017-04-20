# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 21:43:43 2017

@author: Administrator
"""
import cv2  
import numpy as np   
#import matplotlib.pyplot as plt
 
  
img = cv2.imread("000002.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#print img.shape  
grayBlur = cv2.blur(gray, (5, 5))
edges = cv2.Canny(grayBlur, 50, 150, apertureSize= 3)
#edges = cv2.Laplacian(grayBlur, cv2.CV_64F)
#edges = cv2.Sobel(grayBlur, cv2.CV_64F, 1, 1, ksize= 5)

cv2.namedWindow("gray", flags= 0)
cv2.namedWindow("Edges", flags= 0)
cv2.imshow("gray", gray)
cv2.imshow("Edges", edges)

# hough直线检测
#lines = cv2.HoughLines(edges, 1, (np.pi/180), 500)
#
#for rho, theta in lines[0]:
#  a = np.cos(theta)
#  b = np.sin(theta)
#  x0 = a * rho
#  y0 = b * rho
#  x1 = int(x0 + 1000 * (-b))
#  y1 = int(y0 + 1000 * (a))
#  x2 = int(x0 - 1000 * (-b))
#  y2 = int(y0 - 1000 * (a))
#  
#  cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# hough probabilistic transform
minLineLength = 100
maxLineGap = 200
lines = cv2.HoughLinesP(edges, 1, (np.pi / 180), 100,\
                        minLineLength, maxLineGap)

for x1, y1, x2, y2 in lines[0]:
  cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.namedWindow("hough", flags= 0)
cv2.imshow("hough", img)

cv2.waitKey(0)

cv2.destroyAllWindows()