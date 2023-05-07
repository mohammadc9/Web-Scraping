import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

all_info = []

print('Project Started!!')

def func(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')

    posts = soup.find_all('div', class_="main-l panel panel-info")

    

    for i in posts:
        try:
            
            i.find_all('span', dir='ltr')
        
            each_meter_price = re.search("قیمت هر متر مربع:(..\d*)",i.text.strip())
            district=re.search('منطقه(.\d..)',i.text)
            area_by_meter=re.search("زیر بنا: (\d*)",i.text)
            bedrooms=re.search("تعداد اتاق  : (\d*)",i.text)
        
            all_details={'district':district.group(1),'price_per_meter':each_meter_price.group(1),'Area': area_by_meter.group(1),'Rooms':bedrooms.group(1)}
            all_info.append(all_details)
        except AttributeError:
            pass
    return



for m in range (1,15):
    func(f'https://dodota.com/realestate/search/?sort=2&citycode=1&region_code=THR&mantaghe_code=1&v1=1&deal_type=1&page_num={m}')

df=pd.DataFrame(all_info)
df.to_csv('dist1_houses.csv',index=False)


print('End of The Project!!')

