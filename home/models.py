# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
import datetime
from django.db import models
from django.db.models import QuerySet
from decimal import Decimal

#新增的类，将对象,queryset转换成字典
class BaseModel(models.Model):
    class Meta:
        abstract = True
    #将对象转换成字典
    def to_dict(self):
        #内置函数，能够获取对象所有n内容
        #.keys 获取所有变量的名称，返回的是一个列表
        dic = {}
        for key in vars(self).keys():
            # if not key.start干掉__state属性
            if not key.startswith("_"):
                if isinstance(getattr(self, key), datetime.date):
                    dic[key] = datetime.date.strftime(getattr(self, key), '%Y%m%d')
                elif isinstance(getattr(self, key), datetime.datetime):
                    dic[key] = datetime.datetime.strftime(getattr(self, key), '%Y%m%d %H%M%S')
                elif isinstance(getattr(self, key), Decimal):
                    dic[key] = float(getattr(self, key))
                else:
                    dic[key] = getattr(self, key)
        return dic

    @staticmethod
    def qs_to_dict(qs=None):
        """
        将QuerySet对象转化成li套字典
        :param qs:
        :return:
        """
        if isinstance(qs,QuerySet):
            li = [model.to_dict() for model in qs]
        return li

    def to_json(self):
        pass
#轮播图
class Banner(BaseModel):
    bid = models.AutoField(primary_key=True)
    path = models.CharField(max_length=32)

    class Meta:
        db_table = 't_banner'

class Category(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class CategorySub1(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    cid = models.ForeignKey(Category, models.DO_NOTHING, db_column='cid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_sub1'


class CategorySub2(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    cs1id = models.ForeignKey(CategorySub1, models.DO_NOTHING, db_column='cs1id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_sub2'


class Categorysub(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    cid = models.ForeignKey(Category, models.DO_NOTHING, db_column='cid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorysub'


class Order(models.Model):
    ordercode = models.CharField(db_column='orderCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=255, blank=True, null=True)
    post = models.CharField(max_length=255, blank=True, null=True)
    receiver = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    usermessage = models.CharField(db_column='userMessage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    paydate = models.DateTimeField(db_column='payDate', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='deliveryDate', blank=True, null=True)  # Field name made lowercase.
    confirmdate = models.DateTimeField(db_column='confirmDate', blank=True, null=True)  # Field name made lowercase.
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class Orderitem(models.Model):
    pid = models.ForeignKey('Product', models.DO_NOTHING, db_column='pid', blank=True, null=True)
    oid = models.IntegerField(blank=True, null=True)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderitem'


class Product(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(db_column='subTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orignalprice = models.FloatField(db_column='orignalPrice', blank=True, null=True)  # Field name made lowercase.
    promoteprice = models.FloatField(db_column='promotePrice', blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(blank=True, null=True)
    cid = models.ForeignKey(Category, models.DO_NOTHING, db_column='cid', blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'

class Productimage(BaseModel):
    pid = models.ForeignKey(Product, models.DO_NOTHING, db_column='pid', related_name='product_image',blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productimage'


class Property(models.Model):
    cid = models.ForeignKey(Category, models.DO_NOTHING, db_column='cid', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property'


class Propertyvalue(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    ptid = models.ForeignKey(Property, models.DO_NOTHING, db_column='ptid', blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propertyvalue'


class Review(models.Model):
    content = models.CharField(max_length=4000, blank=True, null=True)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    pid = models.ForeignKey(Product, models.DO_NOTHING, db_column='pid', blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'review'


class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
