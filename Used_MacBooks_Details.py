from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver =  webdriver.Chrome()
url='https://divar.ir/s/tehran/laptop-notebook-macbook/apple?goods-business-type=personal'

lists=[]

driver.get(url)
driver.maximize_window()
i = 1
while i < 8:
    driver.execute_script('window.scrollBy(0,1800)','')
    time.sleep(3)
    i=i+1

    posts=driver.find_elements(By.CSS_SELECTOR,'.post-card-item-af972.kt-col-6-bee95.kt-col-xxl-4-e9d46')

    for v in posts:

        title=v.find_element(By.TAG_NAME,'h2').text
        price_date=v.find_elements(By.CSS_SELECTOR,'.kt-post-card__description')
        price=price_date[1].text
        link=v.find_element(By.TAG_NAME,'a').get_attribute('href')
      
        macbook_detail={'name':title,
                      'price':price,
                      'link' : link}

        lists.append(macbook_detail)


#df=pd.DataFrame(lists)
#df.to_csv('macbook_price.csv')
print('Done!')
driver.quit()
