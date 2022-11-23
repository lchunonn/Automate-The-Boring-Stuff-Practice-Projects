import os
from PIL import Image, ImageDraw, ImageFont
import requests

fileobj = open('../automate_online-materials2e/guests.txt')
names = fileobj.read()
names = names.split('\n')

flowerimg_link = requests.get('https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510_960_720.jpg', stream=True)
flowerimg = Image.open(flowerimg_link.raw)
flowerimg = flowerimg.resize((288,360))
os.makedirs('Custom Seating Cards', exist_ok=True)

arialFont = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', size=20)

for name in names:
    im = Image.new('RGBA', (288,360), 'white')
    im.paste(flowerimg)
    draw = ImageDraw.Draw(im)
    draw.rectangle((0,0,288,360),outline='white',width=3)
    textlen = draw.textlength(f"{name}, You're invited!", font=arialFont)
    draw.text(((288-textlen)/2,300), f"{name}, You're invited!", fill='purple', font=arialFont)
    im.save(os.path.join('Custom Seating Cards', f'Invite_{name}.png'))


import pyautogui
pyautogui.click()