
from selenium import webdriver

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



yahoo_url = 'https://tw.buy.yahoo.com/search/product'
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


    for row in content:
        
        link = row.get_attribute('href')
        print(link)