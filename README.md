# Print_Quality_Estimator

# Author: Hunter Obendorfer

This tool allows for a quick and easy way to estimate the quality of a 3D printed object

## Use

1. Testing file are located in the TestCode folder (This code automates running the code with the data set and producing an output)
2. Source files are located in the Source folder
3. The data set is located in the DataSet folder
4. A conda environment is included
5. To test error in object size, the 20mm calibration cube MUST be on the right in the image. Run the 'determineSize.py' file
6. To locate burns/blemishes, run the 'findBurntSpot.py' file
7. To determine elephant's foot, run the 'detectElephantFoot.py'
8. The image files to run these functions must be in the same folder as the python script

A jupyter notebook is included to quickly see the source code in one file

## Conda Environment
Should the conda environment file not work properly, here is a list of necessary packages and their version

1. imutils 0.5.4
2. opencv 3.4.2
3. matplotlib 3.4.3
4. numpy 1.21.2
5. python 3.7.11
6. scikit-image 0.18.3
7. scipy 1.7.2
8. csv

## Data Set Description
A csv is included to compare the results of the functions

Images containing burns/blemishes are located in the 'Burns' folder in the Data Set

Images ready to estimate size (contain the calibration cube) are in the 'DimensionEstimate' folder

Images that have elephant's foot are located in the 'ElephantFoot' folder

Results images are located in 'Results' with a similar file structure, they may or may not be up to date

Note: the first digit in the file name differentiates the type of object, the second digit represents the singular object in that object type. Example, the object group '30' is the third group of objects, with 4 objects 30-33 in the DimenstionEstimate folder
