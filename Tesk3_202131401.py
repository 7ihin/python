# -*- coding: utf-8 -*-

import cv2

fname = "Lighthouse.jpg"
img_gray = cv2.imread(fname, 0) # 0: gray; 1, RGB; -1: transparency
img_color = cv2.imread(fname, 1)

w_new = img_gray.shape[0]//2 # 1000
h_new = img_gray.shape[1]//2 # 500
img_gnew = cv2.resize(img_gray, (300, 300))
img_cnew = cv2.resize(img_color, (300, 300))

# cv2.imshow('Gray', img_gray)
# cv2.imshow('Color', img_color)
cv2.imshow('Gray', img_gnew)
cv2.imshow('Color', img_cnew)

fname_new = "Lighthouse_resized.jpg"
cv2.imwrite(fname_new, img_cnew)
cv2.waitKey(2000) # 0: press button; 2000: 2 seconds
cv2.destroyAllWindows()