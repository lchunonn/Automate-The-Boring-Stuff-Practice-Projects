#! /usr/bin/env python3
import os
from PIL import Image
from pathlib import Path

for foldername, subfolders, filenames in os.walk(Path.home()):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg
        if not (filename.endswith('.png') or filename.endswith('.jpg')):
            numNonPhotoFiles += 1
            continue
        # Open image file using Pillow
        try:
            im = Image.open(os.path.join(Path.home(),foldername,filename))
        except:
            print('Error reading' + os.path.join(foldername, filename))

        # Check if width and height are larger than 500
        if im.size[0] > 500 and im.size[1] > 500:
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo
            numNonPhotoFiles += 1

        # If more than half of files were photos, print the absolute path of the folder

    try:
        if (numPhotoFiles / (numNonPhotoFiles + numPhotoFiles)) > 0.5:
            print(os.path.join(Path.home(),foldername))
    except ZeroDivisionError:
        continue

