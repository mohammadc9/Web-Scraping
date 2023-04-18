from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.indeed.com/cmp/Apple/reviews')
All_info = []
    
while len(All_info)<500:
        
    posts = driver.find_elements(By.CSS_SELECTOR,'.css-t3vkys.eu4oa1w0')

    for v in posts:

        title_content = v.find_elements(By.CSS_SELECTOR, '.css-82l4gy.eu4oa1w0')
        content = title_content[1].text.strip()
        title = title_content[0].text.strip()
        rate = v.find_element(By.CSS_SELECTOR, '.css-1c33izo.e1wnkr790').text

        each_page = {'Title': title, 'Content': content, 'Score': rate}
        All_info.append(each_page)        
    next_button = driver.find_element(By.CSS_SELECTOR, '.css-1brj2y2.e8ju0x50')
    next_button.click()
        
df=pd.DataFrame(All_info)
df.to_csv('indeed.csv')

driver.quit()

print('Done!')
