import os 
import cv2
import numpy as np
import time 
import shutil 
import uuid
img_set = []
folder = r"images\TAU_CANH_SAT_images"
dest = r"images\TAU_CANH_SAT_images_ALL"
os.makedirs(dest, exist_ok=True)
for subfolder_name in os.listdir(folder):
    subfolder_path = os.path.join(folder, subfolder_name)
    for filename in os.listdir(subfolder_path):
        file_path = os.path.join(subfolder_path, filename)
        img_set.append(file_path)

for index, filepath in enumerate(img_set):
    name = str(index)
    shutil.copy(filepath, os.path.join(dest, name + ".png"))