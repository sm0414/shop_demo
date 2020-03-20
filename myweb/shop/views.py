from django.shortcuts import render
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
#   name=''
#   if 'product' in request.GET:
#       name = request.GET['product']
#       if name != '':
#           product_list = getData.getData(name)
#           data = {'product_list':product_list}
#           
#   return render(request,'shop.html',data)
   product=''
   if 'product' in request.GET:
       product = request.GET['product']
       if product != '':
           try:
               data =getData.data_accuracy(product)
               content = {'product_list':data}
           except:
              return render(request,'shop.html')
       else:
           return render(request,'shop.html')
           
       return render(request,'shop.html',content)
   
   else:
       return render(request,'shop.html')
   
def shop_price(request):
#   name=''
#   if 'product' in request.GET:
#       name = request.GET['product']
#       if name != '':
#           product_list = getData.getData(name)
#           data = {'product_list':product_list}
#           
#   return render(request,'shop.html',data)
   product=''
   if 'product' in request.GET:
       product = request.GET['product']
       if product != '':
           try:
               data =getData.data_price(product)
               content = {'product_list':data}
           except:
              return render(request,'shop.html')
       else:
           return render(request,'shop.html')
           
       return render(request,'shop.html',content)
   
   else:
       return render(request,'shop.html')