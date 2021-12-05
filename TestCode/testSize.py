#Hunter Obendorfer
#1834106
#Python 3.7.11, OCV 3.4.2, MPL 3.4.3, numpy 1.21.2
#use high resolution images, I used 4608 × 2592 images

from determineSize import determineSize
import cv2 as cv
import csv

input = "DataSet/DimensionEstimate/dimensions.csv"
output = "DataSet/DimensionEstimate/dimensionsError.csv"
path = "DataSet/DimensionEstimate/"
print("\nOutputting to \'dimenstionError.csv\', all values are percentages.\n")

with open(input, 'r', newline='') as fileToRead:
	readObj = csv.reader(fileToRead)
	header = next(readObj)				#save header
	with open(output, 'w', newline='') as fileToWrite:
		writeObj = csv.writer(fileToWrite)
		writeObj.writerow(header)				#save header to new file
		for row in readObj:
			print("Calculating error for " + row[0])
			#row[0] - file name, row[1] - measured width, row[2] - measured heigth, row[3] - nominal width, row[4] - nominal height
			(width, height) = determineSize(cv.imread(path+row[0]), float(row[3]), float(row[4]), retData=True)

			#calc error, allow negative errors
			#error from nominal value
			nomErrorX = (width - float(row[3]))/float(row[3]) * 100
			nomErrorY = (height - float(row[4]))/float(row[4]) * 100
			#error from measured value
			measErrorX = (width - float(row[1]))/float(row[1]) * 100
			measErrorY = (height - float(row[2]))/float(row[2]) * 100

			#write to file
			list = [row[0], f'{measErrorX:.3f}', f'{measErrorY:.3f}', f'{nomErrorX:.3f}', f'{nomErrorY:.3f}'] #formats floats to 3 decimal places
			writeObj.writerow(list)
		#close output
	#close input
print("\nComplete")