import os, shutil
from pathlib import Path

while True:
    folder = input(f"Enter the filepath of the directory you wish to view, with reference to {Path.home()}.\
    \nTo copy from the {Path.home() / 'Downloads'} folder, type in 'Downloads'\n")
    folder = Path.home() / folder
    if os.path.exists(folder):
        break
    else:
        print(f"{folder} does not exist. Key in an existing directory")

print("The following files are more than 100MB:")
for folder,subfolder,filenames in os.walk(folder):
    for filename in filenames:
        if os.path.getsize(os.path.join(folder,filename)) > 104857600:
            print(folder,filename)
