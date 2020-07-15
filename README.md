# Preprocessing of Histopathology Images

Histopathology refers to microscopic examination of tissue for predicting disease. Digital Histopathology provide tools to examine the digitized specimen slides through virtual microscopy. Glass slides are converted into digital slides and can be viewed, managed, shared and analyzed computationally. Digital pathology is widely being used in diagnostic medicine where deep learning based models may be used for efficient and cheaper diagnoses, prognosis, and prediction of diseases.

Digital pathology Images are often larger with higher resolution, thus handling them for analysis through visualization or preparing for training supervised deep models is required. 
This repository provide utility to preprocess large image files and create a dataset of crops/patches of image.

# About data

For demonstration, wiki histopathology images for benign and malignant lesions are used. However for training on actual histopathology images for particular type of disease, you can download and save images in ``/data`` folder.
For example, histopathoogy images for cancer can be downloaded at [GDC data portal](https://portal.gdc.cancer.gov/)


# Required packages

` $ pip install numpy` 
` $ pip install imageio` 
` $ pip install tifffile` 
` $ pip install imagecodecs`
` $ pip install opencv-python`

# Basic Usage

Download and organize the slide images in data folder as per the class. For example, if you are doing binary classification for cancerous and benign lesions, you may arrange the files as:

* data
  * benign
    * file1.tiff
    * file2.tiff
    * file3.tiff
    * ...
  * malignant
    * file1.tiff
    * file2.tiff
    * file3.tiff
    * ...

` $ python dataset_preprocess.py ` 

This will create a dataset folder `processed_data` with cropped patches (by default of size 256px) of large images in train, test folders. train-test split is 70-30% by default, however you can change it. You can use this dataset to train deep learning models.  
