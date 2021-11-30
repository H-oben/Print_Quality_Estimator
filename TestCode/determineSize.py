import header
#approximate the size of the object and determine how accurate your printer is
#height and width can be found in 3D printer stl slicer, cura has this
#information in the bottom left corner of the screen
#height/width must be in mm
#1 inch = 25.4 mm
#assuming all objects other than the cube are the same object

def determineSize(img, width, height, error=5.0):
    #image must be oriented such that the calibration cube is the rightmost object
    prepared = prepImg(img)
    (h, w) = prepared.shape
    #use otsu's thresholding
    ret, thresh = cv.threshold(prepared, 0,255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    
    #remove small blobs
    thresh = cv.erode(thresh, None, iterations=4)
    thresh = cv.dilate(thresh, None, iterations=8)
    
    #grab contours
    labels = measure.label(thresh, background=0)
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
    cnt = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnt = imutils.grab_contours(cnt)
    
    #find bounding rectangles
    pos = 0
    rightMost = 0
    rect = []
    retImg = img.copy()
    for (i, c) in enumerate(cnt):
        #get min area rectangle and the 4 points
        boundRect = cv.minAreaRect(c) # (center(x,y), (width, height), angle)
        box=cv.boxPoints(boundRect)
        box=np.int0(box)
        cv.drawContours(retImg, [box], 0, (0,255,0), 5)
        
        rect.append(boundRect) #
        if(boundRect[0][0] > rightMost):
            rightMost = boundRect[0][0]
            #label position x of rightmost in rectangle array
            pos=i
    
    #number of pixels for 20 mm
    calibratedX = rect[pos][1][0]
    
    #difference between x and y calibration, perspective is not perfect
    #assuming same depth, subtract the difference from the height to get
    #more accurate estimation
    XYDiff = rect[pos][0][1] - rect[pos][0][0]
    
    #draw bounding rectangles and print sizes/accuracy
    avgErrX = 0.0
    avgErrY = 0.0
    avgH = 0.0
    avgW = 0.0
    for i in range(0, len(rect)):
        if(i != pos):             #ignore cube
            
            #calculate size/error
            sizeX = 20.0 * (rect[i][1][0]/calibratedX)
            sizeY = 20.0 * (rect[i][1][1]/calibratedX)
            errX = (abs(sizeX-width)/width)*100
            errY = (abs(sizeY-height)/height)*100
            
            #add to avgs
            avgErrX = avgErrX+errX
            avgErrY = avgErrY+errY
            avgH = avgH+sizeY
            avgW = avgW+sizeX
            print((sizeX, sizeY, errX, errY))
    
    avgErrX = avgErrX/(len(rect)-1)
    avgErrY = avgErrY/(len(rect)-1)
    avgW=avgW/(len(rect)-1)
    avgH=avgH/(len(rect)-1)
    if(avgErrX>error or avgErrY > error):
        print("Recalibrate steps/mm\nTutorial here: https://all3dp.com/2/how-to-calibrate-a-3d-printer-simply-explained/")
    cv.putText(retImg, 
               "Width: {:.2f} mm, Height: {:.2f} mm, X error: {:.2f}%, Y error: {:.2f}%".format(avgW,avgH,avgErrX,avgErrY),
                (100, h-100), cv.FONT_HERSHEY_PLAIN, 8, (0,255,0), 5)
            
    retImg = cv.cvtColor(retImg, cv.COLOR_BGR2RGB) #cvt before hand
    return(retImg)
