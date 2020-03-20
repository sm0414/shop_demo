#import json
#import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getWeater(city):
#   citys = {'臺北市':0,'新北市':1,'桃園市':2,'臺中市':3,'臺南市':4,'高雄市':5,'基隆市':6,'新竹縣':7,'新竹市':8,'苗栗縣':9,'彰化縣':10,'南投縣':11,'雲林縣':12,'嘉義縣':13,'嘉義市':14,'屏東縣':15,'宜蘭縣':16,'花蓮縣':17,'臺東縣':18,'澎湖縣':19,'金門縣':20,'連江縣':21}
#   response = requests.get("https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWB-BE1D27BE-4C21-406E-A26B-AA5B70F2D141&downloadType=WEB&format=JSON").text
#   result = json.loads(response)
#
#   city = result['cwbopendata']['dataset']['location'][citys[city]]['locationName']
#   weater = result['cwbopendata']['dataset']['location'][citys[city]]['weatherElement'][0]['time'][1]['parameter']['parameterName']
#    driver = webdriver.PhantomJS()
    driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
#    driver = webdriver.Chrome('C://chromedriver.exe')


    driver.get('https://tw.yahoo.com/')
    
    
    try:
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,'uh-profile')))
    finally:
        weater = driver.find_elements_by_css_selector('#uh-profile b')[0].text

    return(city,weater)
   
print(getWeater('台中'))
   
   