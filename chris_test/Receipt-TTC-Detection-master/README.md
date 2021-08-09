##### Extracting total amount TTC on receipt documents

## Context:
The code was written in the case of a data scientist hiring challenge.

@author: Aghiles Azzoug

## Data:
The data (images + json descriptions) can be found on this GitHub repository (https://github.com/clovaai/cord). 

link to the corresponding paper: https://openreview.net/pdf?id=SJl3z659UH

## Using the code:
The executable code can be ran from the `main.ipynb` notebook.

## Python requirements:
Python 3.x with Torch 1.5.1+cu101 (GPU version) and all "classic" packages: numpy, matplotlib etc.

## The main points are:
* Extracting ROI (TTC) bounding boxes from JSON files.
* Resizing all the images to 1296x864 resolution (the most common resolution in the dataset), and I transformed them to channel-first format (for PyTorch conveniance) and reduced the pixels to 0-1 scale.
* The model used is a Faster R-CNN with a ResNet-50 FPN backbone.
* I didn't use Cross-Validation to keep everything simple, I just trained on train data and validated on the test set.
* Some files are taken from Torchvision's GitHub repository (MS-Coco segmentation and prediction part).
