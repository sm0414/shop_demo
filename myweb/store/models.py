from django.db import models


#客戶資料庫
class Customer(models.Model):
    userid = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(null=False, max_length=50)
    password = models.CharField(null=False, max_length=20)
    address = models.CharField(null=False, max_length=100)
    phone = models.CharField(null=False, max_length=20)
    birthday = models.DateField(null=False)

    class Meta:
        db_table = 'Customers'
        ordering = ['userid']


#商品資料庫
class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100)
    price = models.FloatField()
    description = models.CharField(null=True, max_length=200)
    image = models.CharField(null=True, max_length=100)

    class Meta:
        db_table = 'Goods'
        ordering = ['id']


#訂單資料庫
class Orders(models.Model):
    id = models.CharField(primary_key=True, max_length=20, null=False)
    userid = models.CharField(max_length=200, null=False)
    order_date = models.DateTimeField(null=False)
    status = models.IntegerField(default=1, null=False)
    total = models.FloatField(null=False)

    class Meta:
        db_table = 'Orders'
        ordering = ['order_date']


#詳細訂單資料庫
class OrderLineItem(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    userid = models.CharField(max_length=200, null=False)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, null=False)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(default=0, null=False)
    sub_total = models.FloatField(default=0.0, null=False)

    class Meta:
        db_table = 'OrderLineItems'
        ordering = ['id']
