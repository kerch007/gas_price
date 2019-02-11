import pandas as pd
import pytesseract
import cv2
import numpy as np
from PIL import Image, ImageOps


basewidth = 1800
img = Image.open('/home/kerch007/PycharmProjects/Stella/stella_api/gas_price.png')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
data = pytesseract.image_to_string(img, config='--psm 6 --oem 3')

df = data.split("\n")
df = pd.DataFrame([sub.split(" ") for sub in df])
df = df.drop(df.columns[[8]], axis=1)
df = df.dropna(how='any',axis=0)
df.index =['Авиас','Авиас плюс','Укрнафта','Sentoza Oil','Neftek',
'Юкон','SUN OIL','Формула','UPG','AMIC','ТНК','БРСМ-нафта','Shell','ОККО','WOG',
'SKY','Glusco','Автотранс']
df.columns = ['A98','A95+','A95','A92','A80','ДТ','ДТ+','ГАЗ']
df = df.replace(('=',':'),'-')

print(df)