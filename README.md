# MRI Segmentation ACDC project

## Description
This project segments the right ventricle, myocardium, and left ventricle of MRI scans.

## Usage

Open a Jupyter Lab environment and download all files in the repository and place
them in one folder. Open the notebook `acdc_main.ipynb`. In cell 3, change the
data path to one where your data set is found.

Running all cells in the code will perform cross-validation, train a U-net from 
the start and finish with segmenting the test set. If only segmentation is desired 
it suffices to run the following cells:
- All imported libraries
- The variable with the data path
- The function call to unzip all images
- The function definitions that create a dictionary and loads the data
- The transforms
- The definition of the device
- The test dictionaries
- The model definition
- The loading of parameters with the correct data path to the trained model
- The compute_metric function definition
- The compute_metric function call
