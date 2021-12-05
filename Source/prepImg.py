#Hunter Obendorfer
#1834106
#Python 3.7.11, OCV 3.4.2, MPL 3.4.3, numpy 1.21.2
#use high resolution images, I used 4608 × 2592 images

import cv2 as cv
import numpy as np

#prepare image
def prepImg(img):
    #cvt to gray
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #blur
    blurred = cv.GaussianBlur(imgGray, (13,13), 0)
    #sharpen
    k = np.array([[0, -1, 0],
                  [-1, 5, -1],
                  [0, -1, 0]])
    sharp = cv.filter2D(blurred, -1, kernel=k)
    #Normalize grayscale to 0-255
    norm = cv.normalize(blurred, None, alpha = 0, beta = 255, norm_type = cv.NORM_MINMAX)
    return(norm)
