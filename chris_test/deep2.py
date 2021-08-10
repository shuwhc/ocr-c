

def json_to_pascal(json, filename): #filename is the .mat file
    # convert json to pascal and save as csv
    pascal_list = []
    for i in json:
        for j in range(len(i['labels'])):
            pascal_list.append({'fname': i['filename'] 
            ,'xmin': int(i['left'][j]), 'xmax': int(i['left'][j]+i['width'][j])
            ,'ymin': int(i['top'][j]),  'ymax': int(i['top'][j]+i['height'][j])
            ,'class_id': int(i['labels'][j])})
    df_pascal = pd.DataFrame(pascal_list,dtype='str')
    df_pascal.to_csv(filename,index=False)
p = read_process_h5(file_path)
json_to_pascal(p, data_folder+'pascal.csv')

def viz_random_image(df):
    file = np.random.choice(df.fname)
    im = skimage.io.imread(data_folder+file)
    annots =  df[df.fname==file].iterrows()
    plt.figure(figsize=(6,6))
    plt.imshow(im)
    current_axis = plt.gca()
    for box in annots:
        label = box[1]['class_id']
        current_axis.add_patch(plt.Rectangle(
            (box[1]['xmin'], box[1]['ymin']), box[1]['xmax']-box[1]['xmin'],
            box[1]['ymax']-box[1]['ymin'], color='blue', fill=False, linewidth=2))  
        current_axis.text(box[1]['xmin'], box[1]['ymin'], label, size='x-large', color='white', bbox={'facecolor':'blue', 'alpha':1.0})
        plt.show()
viz_random_image(df)

import os
import sys
import skimage.io
import scipy
import json
with open('json_config.json') as f:     json_conf = json.load(f)
ROOT_DIR = os.path.abspath(json_conf['ssd_folder']) # add here mask RCNN path
sys.path.append(ROOT_DIR)

import cv2
from utils_ssd import *
import pandas as pd
from PIL import Image

from matplotlib import pyplot as plt

%matplotlib inline
%load_ext autoreload
% autoreload 2

task = 'svhn'
labels_path = f'{data_folder}pascal.csv'
input_format = ['class_id','image_name','xmax','xmin','ymax','ymin' ]
    
df = pd.read_csv(labels_path)

class SVHN_Config(Config):
    batch_size = 8
    
    dataset_folder = data_folder
    task = task
    
    labels_path = labels_path

    input_format = input_format

conf=SVHN_Config()

resize = Resize(height=conf.img_height, width=conf.img_width)
trans = [resize]