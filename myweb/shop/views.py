from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import getData
from . import getWeater

def index(request):
   city=''
   if 'city' in request.GET:
       city = request.GET['city']
       if city != '':
           try:
               c,w = getWeater.getWeater(city)
               content = {'weater':c+'天氣:'+w}
           except:
               content = {'weater':'請確認是否有錯字'}
       else:
           content = {'weater':'請輸入城市'}
   else:
       content = {'weater':''}
   return render(request,'index.html',content)


def shop(request):
   global product
   if 'product' in request.GET:
       product = request.GET['product']
       if product != '':
           if 'sortby' in request.GET:
               try:
                   product_list =getData.data_price(product)
                   content = {'product_list':product_list,'product':product}

                   return render(request,'shop.html',content)
               except:
                   return render(request,'shop.html')
           else:
               try:
                   product_list =getData.data_accuracy(product)
                   content = {'product_list':product_list,'product':product}

                   return render(request,'shop.html',content)
               except:
                  return render(request,'shop.html')
       else:
            return redirect('/shop')
   else:
       return render(request,'shop.html')

"""
def price(request):
   global product
   if 'product' in request.GET:
       product = request.GET['product']

       if product != '':
           try:
               data =getData.data_price(product)
               content = {'product_list':data}
               return render(request,'shop.html',content)
           except:
               return render(request,'shop.html')
   else:
       try:
           data =getData.data_price(product)
           content = {'product_list':data}
           return render(request,'shop.html',content)
       except:
           return render(request,'shop.html')
"""
