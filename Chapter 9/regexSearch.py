import os
import re
from pathlib import Path

desktop_dir = os.path.join(Path.home(), 'Desktop')
files = os.listdir(desktop_dir)
txt_files = []
for file in files:
    if file.endswith('.txt'):
        txt_files.append(file)

regex_input = input("Enter your regex: ")
regex = re.compile(rf'{regex_input}')
include_regex_files = []

for txt_file in txt_files:
    f=open(os.path.join(desktop_dir, txt_file))
    string = f.read()
    if regex.search(string):
        include_regex_files.append(txt_file)

print(include_regex_files)