from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

driver = webdriver.Chrome()
img_link = []
data = []
df = pd.read_csv('links.csv')
pages = df['Link'].values.tolist()

j=1
for page in pages:
    print(j)
    j += 1
    driver.get(page)
    imgs = driver.find_elements(By.CLASS_NAME,"owl-stage")[0].find_elements(By.CLASS_NAME,'owl-item')
    links=[]
    for img in imgs:
        image_link = img.find_element(By.TAG_NAME,'div').find_element(By.TAG_NAME,'a').get_attribute('href')
        img_link.append(image_link)
        
        a = image_link[::-1]
        b = a.find('/') 
        c = a[b+1:]
        d = c.find('/')
        e = a[:b+d]
        f = e[::-1]
        # print(f)
        links.append(f)
    name = driver.find_element(By.XPATH,'//h1[contains(@class,"h2")]').text
    price = driver.find_element(By.XPATH,"//span[contains(@class,'new-price')]").text
    description = driver.find_element(By.ID,'description').text
    data.append([name,description,price,links])
df = pd.DataFrame(data=data,columns = ['Product Name','Description','Price','Images'])

img = df['Images']
def rep(data):
    x = data.replace('[','')
    y = x.replace(']','')
    z = y.replace("'",'')
    return z
df['Images'] = df['Images'].apply(lambda x: rep(x))
print(df.head())
df.to_csv('info.csv',index=False)
imgdf = pd.DataFrame(data=img_link,columns=['link'])
imgdf.to_csv('img_link.csv',index=False)
# print(len(imgs))



