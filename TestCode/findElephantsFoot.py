#Hunter Obendorfer
#1834106
#Python 3.7.11, OCV 3.4.2, MPL 3.4.3, numpy 1.21.2
#use high resolution images, I used 4608 × 2592 images

import cv2 as cv
from prepImg import prepImg

#detect elephant's foot

#splitting images https://oleksandrg.medium.com/how-to-divide-the-image-into-4-parts-using-opencv-c0afb5cab10c

#TODO: make more robust using this method
#https://stackoverflow.com/questions/37177811/crop-rectangle-returned-by-minarearect-opencv-python
def findElephantFoot(img, error=5.0, retData=False):
    errorMSG = "Elephant's foot detected, re-level the print bed.\nGuide here: https://all3dp.com/2/3d-printer-bed-leveling-step-by-step-tutorial/\nThe author of this software recommends using feeler gauges, not paper to re-level the bed."
    prep = prepImg(img)
    #split image, use right side only
    (origH, origW) = prep.shape
    
    #take right side
    rightSide = prep[:, origW//2 :]
    
    #use otsu's thresholding
    ret, thresh = cv.threshold(rightSide, 0,255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    
    #take average
    (h, w) = thresh.shape
    whitePixels = 0
    blankLines = 0
    for y in range(int(h/2)): #loop through top half only
        for x in range(w): 
            if(thresh[y][0] == 0):
                blankLines+=1
                break
            if(thresh[y][x] == 0):
                break #small optimization
            else:
                whitePixels += 1
    avg = whitePixels / ((h/2.0)-blankLines)
    #find elephant foot
    for y in range(int(h/2),h): #bottom half
        rowCount=0 #num white pixels in row
        if(thresh[y][0] == 0):
            print("Found bottom")
            break

        for x in range(w):
            if(thresh[y][x] == 0): 
                break
            else:
                rowCount+=1
        #calculate error
        measuredError = ((rowCount-avg)/avg)*100 #allows to ignore negative errors
        if(measuredError >= error): #only consider error greater than average
            if(retData):
                return(1)
            else:
                print(errorMSG)
            break
    return(0)