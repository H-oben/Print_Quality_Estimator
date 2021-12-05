#Hunter Obendorfer
#1834106
#Python 3.7.11, OCV 3.4.2, MPL 3.4.3, numpy 1.21.2
#use high resolution images, I used 4608 × 2592 images

from findElephantsFoot import findElephantFoot
import csv
import cv2 as cv
path = "DataSet/ElephantFoot/"
input = path+ "ElephantsFoot.csv"
output = path+ "FootOut.csv"

print("Outputting to \'" +output+ "\', 0 = incorrect result, 1 = correct result.")

with open(input, 'r', newline='') as fileToRead:
	readObj = csv.reader(fileToRead)
	header = next(readObj)

	with open(output, 'w', newline='') as fileToWrite:
		writeObj = csv.writer(fileToWrite)
		writeObj.writerow([header[0], "Correct Result"])
		for row in readObj:
			print("Finding Elephant's Foot in " + row[0])
			#row[0] - file name, row[1] - has elephant's foot, 0 = False, 1 = True
			result = findElephantFoot(cv.imread(path+row[0]), retData=True)
			if(result == int(row[1])):
				writeObj.writerow([row[0], 1])
			else:
				writeObj.writerow([row[0], 0])
		#close write
	#close read
print("Complete")