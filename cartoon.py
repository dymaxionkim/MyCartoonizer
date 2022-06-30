# https://github.com/lutianming/cartoonizer
#
# Prerequitites : numpy scipy opencv-python cartooner
# Build exe : pyinstaller -w -F cartoon.py (Not Successful)
#
from cartooner import cartoonize
import cv2
import os
import time

path_dir = '.'
file_list = os.listdir(path_dir)

for file_name in file_list:
    file_name_head, file_name_ext = os.path.splitext(file_name)
    if file_name_ext==".jpg" or file_name_ext==".png":
        print(file_name)
        file_name_output = file_name_head+"_cartoon"+".png"
        image = cv2.imread(file_name)
        output = cartoonize(image)
        cv2.imwrite(file_name_output, output)

print("Finished!")
