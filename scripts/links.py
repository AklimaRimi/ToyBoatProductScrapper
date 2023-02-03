from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

driver = webdriver.Chrome()

data = []

for i in range(1,5):
    url = f'https://www.rue-des-maquettes.com/maquettes-par-theme/maquettes-voiliers.c1019.html?page={i}'
    driver.get(url)
    
    links = driver.find_elements(By.XPATH,"//div[contains(@class,'cube-produit')]")
    for link in links:
        try:
            x = link.find_element(By.TAG_NAME,'a').get_attribute('href')
            data.append(x)
        except:
            continue
    
    print('finish')
df = pd.DataFrame(data=data,columns=['Link'])
df.to_csv('links.csv',index=False)