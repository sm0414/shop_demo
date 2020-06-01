# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:51:46 2020

@author: vincent
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib

yahoo_url = 'https://tw.buy.yahoo.com/search/product'
momo_url = 'https://m.momoshop.com.tw/search.momo'
pchome_url = 'https://ecshweb.pchome.com.tw/search/v3.3'

def search_yahoo(product):

    param = {'p':product}
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

    response = requests.get(yahoo_url,headers=header,params=param).text
    soup = BeautifulSoup(response,'html.parser')

    items = []
    i=0
    for row in soup.find_all('li',class_='BaseGridItem__grid___2wuJ7'):
        if (i<15):
            item = {}

            img = row.find('img').get('srcset')
            img = img.split(',')
            img = img[0].lstrip()
            img = img.split(' ')
            name = row.find('span',class_='BaseGridItem__title___2HWui').text
            price = row.find('em').text
            price = price.strip('$')
            price = price.replace(',','')
            link = row.find('a',class_='BaseGridItem__content___3LORP BaseGridItem__hover___3UlCS').get('href')

            item['webname'] = 'Yahoo購物中心'
            item['pname'] = name
            item['price'] = int(price)
            item['link'] = link
            item['img'] = img[0]

            items.append(item)
        i+=1

    return items

def search_momo(product):

    params = {'searchKeyword':product,'couponSeq':'','searchType':'1','cateLevel':'-1','ent':'k','_imgSH':'fourCardStyle'}
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Cookie': '_ga=GA1.3.1990474752.1584021634; _gid=GA1.3.736209732.1584021634; _mwa_uniCampaignInfo=1584021634295464449.1584021634295; __auc=12944eff170cf0bfd0896723e64; bid=e3ef04eff71605fc6a22ddfe3fba07ca; isBI=1; _atrk_siteuid=BfF8DyLT3ugOCpLx; TN=undefined; CN=undefined; CM=undefined; _gcl_au=1.1.851107694.1584021641; appier_utmz=%7B%22csr%22%3A%22www.momoshop.com.tw%22%2C%22timestamp%22%3A1584021639%2C%22lcsr%22%3A%22www.momoshop.com.tw%22%7D; NSC_MC-n.npnptipq.dpn.ux*80=ffffffff0952530345525d5f4f58455e445a4a4229a0; ARK_ID=JS58cdeacd9da172bdd7c6f8bcf42424d358cd; shoppingCartItem=0; coverPlateAd=1; _tam=F_ka1rjl6qBUMQudz8KFZ-pw; _fbp=fb.3.1584021789677.1520006482; _fbp=fb.3.1584021789677.1520006482; __BWfp=c1584021789778x7ce764401; _bworgid=CJR20200312220043860424; pwaLifeCircle=1; Tagtoo_pta=pta_03+_&gpa+_&gpb+_&gpc+_&vip+_; showFilterBtn=0; imgSH=fourCardType; GoodsBrowsingHistory=%5B%223978791%22%5D; _TUCI_T=sessionNumber+18333&pageView+18333&productPageView+18333; _TUCI=sessionNumber+1000&ECId+1039&hostname+m.momoshop.com.tw&pageView+2000&productPageView+1000; _ga=GA1.4.1990474752.1584021634; _gid=GA1.4.736209732.1584021634; JSESSIONID=766D8301D5CA962879700C9555757EF5-m1.b1-mobileap18; _mwa_uniVisitorInfo=1584021634294383046.1584021634294.2.1584024341953; _mwa_uniSessionInfo=1584024341952317806.1584024341952.1.1584024341953; __asc=2ee5eb01170cf354dd926f41024; _atrk_ssid=SxXhENyhja9qLKeEnQloAA; _atrk_sessidx=1; appier_pv_counterERlDyPL9yO7gfOb=7; appier_page_isView_ERlDyPL9yO7gfOb=f7407d9381d4b42b59295ee35c7aa19dd0181bdb09e6963bc0d044db6088161d',
'Host': 'm.momoshop.com.tw',
'Referer': 'https://m.momoshop.com.tw/search.momo?searchKeyword=%E5%8F%A3%E7%BD%A9&couponSeq=&searchType=1&cateLevel=-1&ent=k&_imgSH=fourCardStyle',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

    res = requests.get(momo_url,headers=headers,params=params).text
    soup = BeautifulSoup(res,'html.parser')

    items = []
    i=0
    for row in soup.find_all(class_='goodsItemLi'):
        if (i<15):
            item = {}
            name = row.find('p','prdName').text
            price = row.find('b','price').text.replace(',','')
            if not price:
                continue
            link= 'https://m.momoshop.com.tw' + row.find('a').get('href')
            img = row.find('img').get('src')

            price = price.replace('$','')
            name = name.strip()

            if price != '熱銷一空':
                item['webname'] = 'momo購物網'
                item['pname'] = name
                item['price'] = int(price)
                item['link'] = link
                item['img'] = img

                items.append(item)
        i+=1

    return items

def search_pchome(product):
#    driver = webdriver.PhantomJS(executable_path='C://phantomjs.exe')
#    driver = webdriver.Chrome('C://chromedriver.exe')
    driver = webdriver.PhantomJS()

    encodedProduct = urllib.parse.quote(product)
    driver.get('https://ecshweb.pchome.com.tw/search/v3.3/?q='+encodedProduct+'&scope=all&sortParm=rnk&sortOrder=dc')


    try:
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,'ItemContainer')))
        time.sleep(1)
    finally:
        content = driver.find_elements_by_css_selector('#ItemContainer dl')
        i=0
        items = []

        for row in content:
            if (i<15):
                item = {}
                name = row.find_elements_by_css_selector('.prod_name a')[0].text
                link = row.find_elements_by_css_selector('.prod_name a')[0].get_attribute('href')
                img = row.find_elements_by_css_selector('.prod_img img')[0].get_attribute('src')
                price = row.find_elements_by_css_selector('.price span')[0].text

                item['webname'] = 'PChome線上購物'
                item['pname'] = name
                item['price'] = int(price)
                item['link'] = link
                item['img'] = img

                items.append(item)

            i+=1
    driver.close()
    return items

print(search_momo('口罩'))
