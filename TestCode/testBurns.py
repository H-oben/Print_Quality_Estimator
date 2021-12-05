#Hunter Obendorfer
#1834106
#Python 3.7.11, OCV 3.4.2, MPL 3.4.3, numpy 1.21.2
#use high resolution images, I used 4608 × 2592 images

from findBurntSpot import findBurntSpot
import cv2 as cv
import csv

print("\nNote: Currently, the findBurntSpot function is expected to find burns on the object even when they are not present.")
print("This function still needs inprovement but it will find burns that are blothces.")
print("Also note that this process is very slow due to custom thresholding.\n")

path = "DataSet/Burns/"
input = path+"hasBurns.csv"
output = path+"burnsFound.csv"

print("Outputting to " + output + "\n")

with open(input, 'r', newline='') as fileToRead:
	readObj = csv.reader(fileToRead)
	header = next(readObj)
	with open(output, 'w', newline='') as fileToWrite:
		writeObj = csv.writer(fileToWrite)
		writeObj.writerow(header)
		for row in readObj:
			print("Finding burns in " + row[0])
			cnt = findBurntSpot(cv.imread(path+row[0]), retData=True)
			if(len(cnt) > 0):
				writeObj.writerow([row[0], 1])
			else:
				writeObj.writerow([row[0], 0])
		#close write
	#close read
print("\nComplete")
