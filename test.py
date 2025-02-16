import os 
import cv2
import numpy as np
import time 
def check_duplicate(image1, image2):
    # Check if the images have the same shape and size
    if image1.shape == image2.shape:
        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)  # If all pixels are the same, result is True
    else:
        result = False
    return result
img_set = []
folder = r"images\TAU_CA_images"
for subfolder_name in os.listdir(folder):
    subfolder_path = os.path.join(folder, subfolder_name)
    for filename in os.listdir(subfolder_path):
        file_path = os.path.join(subfolder_path, filename)
        image1 = cv2.imread(file_path)
        print ('processing: ', file_path)
        for image2 in img_set:
            res = check_duplicate(image1, image2)
        if img_set == []:
            img_set.append(image1)
            continue
        if res:
            print ('duplicate')
            time.sleep(10)
        else:
            img_set.append(image1)