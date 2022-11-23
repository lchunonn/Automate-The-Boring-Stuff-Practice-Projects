import os, shutil
from pathlib import Path

while True:
    source = input(f"Enter the filepath of the directory you wish to copy from, with reference to {Path.home()}.\
    \nTo copy from the {Path.home() / 'Downloads'} folder, type in 'Downloads'\n")
    source = Path.home() / source
    if os.path.exists(source):
        print(source)
        break
    else:
        print(f"{source} does not exist. Key in an existing directory")

extension = input("Enter the file extension that you wish to copy.\nTo copy jpg files, type 'jpg'\n")
destination = input(f"Enter the filepath of the directory you wish to copy to, with reference to {Path.home()}.\n")
destination = Path.home() / destination

if not os.path.exists(destination):
    os.makedirs(destination)
    print(f"{destination} does not exist. Creating {destination}")
print(f"Copying .{extension} files from {source} to {destination}")

i=0
for folder, subfolder, filenames in os.walk(source):
    for filename in filenames:
        if str(folder) == str(destination): #str because Posixpath and os path are not equal
            continue
        if filename.endswith(extension):
            try:
                shutil.copy(os.path.join(folder, filename), destination)
                i+=1
            except shutil.SameFileError:
                print(f"{filename} already exists. Skipping {os.path.join(folder, filename)}")
            except:
                print(f"Something went wrong. {os.path.join(folder, filename)}")