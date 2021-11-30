# Print_Quality_Estimator

# Author: Hunter Obendorfer

This tool allows for a quick and easy way to estimate the quality of a 3D printed object

## Use

1. Testing file are located in the TestCode folder
2. Source files are located in the Source folder
3. The data set is located in the DataSet folder
4. A conda environment is included
5. To test error in object size, the 20mm calibration cube MUST be on the right in the image. Run the 'determineSize.py' file
6. To locate burns/blemishes, run the 'findBurntSpot.py' file
7. To determine elephant's foot, run the 'detectElephantFoot.py'
8. The image files to run these functions must be in the same folder as the python script

## Conda Environment
Should the conda environment file not work properly, here is a list of necessary packages and their version

1. imutils 0.5.4
2. opencv 3.4.2
3. matplotlib 3.4.3
4. numpy 1.21.2
5. python 3.7.11
6. scikit-image 0.18.3
7. scipy 1.7.2
