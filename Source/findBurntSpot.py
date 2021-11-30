import header

#find burnt pieces of filament lodged in the object
#This is a result of an unclean nozzle
#cannont detect line-like burns, only blob like
def findBurntSpot(img, objectColor = "white"):
    #unused for now, only considering objects made from white filament 
    #objectColor.lower()
    prepared = prepImg(img)
    #since brown is only slightly darker, a value that is not 0 or 255 should be
    #a burnt piece of filament embedded in the print
    #220 is a good value to use, found by testing
    
    #do range thresholding
    #change values in range to 255
    #values not in range are set to 0
    
    for x in range(0,width):
        for y in range(0, height):
            if(prepared[y][x] < 214):
                prepared[y][x] = 0
            elif (prepared[y][x] > 220):
                prepared[y][x] = 0
            else:
                prepared[y][x] = 255
    #^makes a half decent edge detector
    #remove small blobs
    prepared = cv.erode(prepared, None, iterations=4)
    prepared = cv.dilate(prepared, None, iterations=8)
    
    #remove edges, implement later
    #edges = cv.Canny(thresh, 50, 150)
    #thresh = thresh-edges
    
    #find blobs using connected component analysis
    #found here https://www.pyimagesearch.com/2016/10/31/detecting-multiple-bright-spots-in-an-image-with-python-and-opencv/
    
    labels = measure.label(prepared, background=0)
    mask = np.zeros(prepared.shape, dtype='uint8')
    for label in np.unique(labels):
        if label == 0:
            continue
        labelMask = np.zeros(prepared.shape, dtype='uint8')
        labelMask[labels == label] = 255
        numpixels = cv.countNonZero(labelMask)
        if(numpixels >= 4000):
            mask = cv.add(mask, labelMask)
    
    #finds contours
    contours = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    if(len(contours) > 0):
        print("Burns/blemishes found, clean the printer's nozzle inside and out.")
    return(contours)
