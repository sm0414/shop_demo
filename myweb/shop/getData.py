# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:10:49 2020

@author: vincent
"""

from . import scraping_price
from . import scraping_accuracy
#import scraping_price
#import scraping_accuracy

def data_price(product):
    yahoo_data = scraping_price.search_yahoo(product)
    momo_data = scraping_price.search_momo(product)
    pchome_data = scraping_price.search_pchome(product)

    alldata = []

    for y,m,p in zip(yahoo_data,momo_data,pchome_data):
        alldata.append(y)
        alldata.append(m)
        alldata.append(p)


    contents = sorted(alldata, key=lambda i: i['price'])

    return contents


def data_accuracy(product):
    yahoo_data = scraping_accuracy.search_yahoo(product)
    momo_data = scraping_accuracy.search_momo(product)
    pchome_data = scraping_accuracy.search_pchome(product)


    alldata = []

    for y,m,p in zip(yahoo_data,momo_data,pchome_data):
        alldata.append(y)
        alldata.append(m)
        alldata.append(p)


#    contents = sorted(alldata, key=lambda i: i['price'])

    return alldata

#print(data_accuracy('口罩'))
