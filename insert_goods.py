
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
#import pymysql
import psycopg2


yahoo_url = 'https://tw.buy.yahoo.com/search/product'

#conn = pymysql.connect(host='localhost',user='root',password='123456789',database='myStore',charset='utf8')
conn = psycopg2.connect(host='localhost',user='vlgtejrtqaifoy',password='79c2bd67336e4fd7d96cf58ff970d42068dd05367ae5500d67e7f7bb45b578fb',database='dc35ssjrafc4hp',port='5432')

cursor = conn.cursor()

def search_yahoo(product):  
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("window-size=1024,768")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(chrome_options=options)
#    driver = webdriver.PhantomJS(executable_path='C:/phantomjs.exe')
    driver.get('https://tw.buy.yahoo.com/search/product?p='+product)
    
    n = [4,2,1.5,1.3]
    
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'isoredux-root')))
        time.sleep(1)
        for i in n:
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight/%d)'%(i))
            time.sleep(1)
    finally:
        content = driver.find_elements_by_css_selector('.BaseGridItem__grid___2wuJ7 a')

    items = []
    for row in content:
        
        link = row.get_attribute('href')
        
        
        
        items.append(link)
    
    aa(items)

def aa(items):
    header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'B=4moinr5f6kg3r&b=3&s=go; GUC=AQEBAQFea5FedEIguASi; A1=d=AQABBHtAal4CEA-Y3Kw7D1PNYjqK5NlXYksFEgEBAQGRa150XgAAAAAA_SMAAAcIe0BqXtlXYks&S=AQAAAkSk34F73p2J9PGoJ758NOw; A3=d=AQABBHtAal4CEA-Y3Kw7D1PNYjqK5NlXYksFEgEBAQGRa150XgAAAAAA_SMAAAcIe0BqXtlXYks&S=AQAAAkSk34F73p2J9PGoJ758NOw; _ga=GA1.3.524308248.1584021631; _gid=GA1.3.316965094.1584021631; APID=UP271f8795-646a-11ea-983c-0a59331d0a5e; APIDTS=1584021792; _gat=1; A1S=d=AQABBHtAal4CEA-Y3Kw7D1PNYjqK5NlXYksFEgEBAQGRa150XgAAAAAA_SMAAAcIe0BqXtlXYks&S=AQAAAkSk34F73p2J9PGoJ758NOw&j=WORLD',
'Host': 'tw.buy.yahoo.com',
'Referer': 'https://tw.buy.yahoo.com/search/product?p=%E5%8F%A3%E7%BD%A9',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
#    print(len(items))
    for item in items:
        
        response = requests.get(item,headers=header).text
        soup = BeautifulSoup(response,'html.parser')
        
        try:
            ds = soup.find('div',class_='ShoppingProductFeatures__productFeatureWrapper___1D0EZ')
            d = ds.find_all('li')
            description = ''
            
            for row in d:
                n = row.text
                n = n.lstrip()
                n = n.rstrip()
                description += n+'\n'
        except:
            print('錯誤')
        

        
        
        name_img = soup.find('div',class_='ProductItemPage__imgSectionWrap___1WJEP')
        name = name_img.find('img').get('alt')
        image = name_img.find('img').get('src')
        price = soup.find('div',class_='HeroInfo__mainPrice___H9A5r').text
        price = price.replace('$','')
        price = price.replace(',','')
        
#        print(name)
#        print(price)
#        print(description)
#        print(image)
#        print('-'*30)

        sql = "insert into Goods(name,price,description,image) values(%s,%s,%s,%s)"
        cursor.execute(sql,[name,float(price),description,image])
        conn.commit()
        
    cursor.close()
    conn.close()
    

search_yahoo('筆電')
