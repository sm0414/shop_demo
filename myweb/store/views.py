from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
import random
import datetime

from .forms import LoginForm, RegistrationForm
from .models import Customer, Goods, OrderLineItem, Orders


#登錄
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data['userid']
            password = form.cleaned_data['password']
            c = Customer.objects.filter(userid=userid)

            if len(c) > 0:
                if c[0].password == password:
                    #加入session
                    request.session['customer_id'] = c[0].userid
                    return HttpResponseRedirect('/store/main/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


#註冊
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            customer = Customer()
            customer.userid = form.cleaned_data['userid']
            customer.name = form.cleaned_data['name']
            customer.password = form.cleaned_data['password1']
            customer.birthday = form.cleaned_data['birthday']
            customer.address = form.cleaned_data['address']
            customer.phone = form.cleaned_data['phone']

            customer.save()

            return render(request, 'customer_reg_success.html')
    else:
        form = RegistrationForm()

    return render(request, 'customer_reg.html', {'form': form})


def main(request):
    if not request.session.has_key('customer_id'):
        return HttpResponseRedirect('/store/login/')

    return render(request, 'main.html')


class GoodsListView(ListView):
    model = Goods
    ordering = ['id']
    template_name = 'goods_list.html'


def show_goods_detail(request):
    goodsid = request.GET['id']
    goods = Goods.objects.get(id=goodsid)

    return render(request, 'goods_detail.html', {'goods': goods})


#加入購物車
def add_cart(request):
    if not request.session.has_key('customer_id'):
        return HttpResponseRedirect('/store/login/')

    goods_id = int(request.GET['id'])
    goods_name = request.GET['name']
    goods_price = float(request.GET['price'])

    #判斷session是否已有購物車
    if not request.session.has_key('cart'):
        request.session['cart'] = []

    cart = request.session['cart']
    flag = 0

    for item in cart:
        if item[0] == goods_id:
            item[3] += 1
            flag = 1
            break

    if flag == 0:
        #添加新商品至購物車
        item = [goods_id, goods_name, goods_price, 1]
        cart.append(item)

    request.session['cart'] = cart

    page = request.GET['page']
    if page == 'detail':
        return HttpResponseRedirect('/store/detail/?id=' + str(goods_id))
    else:
        return HttpResponseRedirect('/store/list/')


def show_cart(request):
    if not request.session.has_key('customer_id'):
        return HttpResponseRedirect('/store/login/')

    if not request.session.has_key('cart'):
        return render(request, 'cart.html', {'list': [], 'total': 0.0})

    cart = request.session['cart']
    list = []
    total = 0.0
    for item in cart:
        subtotal = item[2] * item[3]
        total += subtotal
        new_item = (item[0], item[1], item[2], item[3], subtotal)

        list.append(new_item)

    return render(request, 'cart.html', {'list': list, 'total': total})


def submit_orders(request):
    if request.method == 'POST':
        
        cart = request.session['cart']
        userid = request.session['customer_id']
        
        orders = Orders()
        i = random.randint(0, 9)
        d = datetime.datetime.now()
        ordersid = str(int(d.timestamp() * 1e6)) + str(i)
        orders.id = ordersid
        orders.userid = userid
        orders.order_date = d
        orders.status = 1
        orders.total = 0.0
        orders.save()

        total = 0.0

        for item in cart:
            goodsid = item[0]
            goods = Goods.objects.get(id=goodsid)
            
            #在網頁上更新後的數量
            quantity = request.POST['quantity_' + str(goodsid)]

            try:
                quantity = int(quantity)
            except:
                quantity = 0

            subtotal = item[2] * quantity
            total += subtotal

            order_line_item = OrderLineItem()
            order_line_item.quantity = quantity
            order_line_item.userid = userid
            order_line_item.goods = goods
            order_line_item.orders = orders
            order_line_item.sub_total = subtotal

            order_line_item.save()

        orders.total = total
        orders.save()

        del request.session['cart']

        return render(request, 'order_finish.html', {'ordersid': ordersid})


def logout(request):
    if request.session.has_key('customer_id'):
        del request.session['customer_id']
        if request.session.has_key('cart'):
            del request.session['cart']

    return HttpResponseRedirect('/store/login/')
