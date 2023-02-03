from fastbook import *
import pandas as pd
import os
import urllib.request
import time
from PIL import Image

df = pd.read_csv('img_link.csv')
links = df['link'].values.tolist()
j = 0
for link in links:
    print(link,j)
    j += 1
    a = link[::-1]
    b = a.find('/') 
    img = a[:b]
    img = img[::-1]
    c = a[b+1:]
    d = c.find('/')
    e = a[b+1:b+d+1]
    e = e[::-1]



    path = f'images/{e}'
    if os.path.exists(path) == False:
        os.mkdir(path)
    urllib.request.urlretrieve(link, f"{path}/{img}")


    