import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render

# 序列化   ---- 生成json数据
# 反序列化 ----- 解析json数据
from home.models import Product, Productimage, Category, Categorysub, Banner, BaseModel


# 前后端分离,返回的时候不是模板 而是json数据
# python  对象 不支持json

#接口1 search
def get_search_shop(request):
    result = {}
    try:
        keywords = request.GET.get('key')
        #products是queryset对象，里面包含2个对象
        products = Product.objects.filter(name__contains=keywords)
        li = []
        for product in products:
            product.img_list = product.qs_to_dict(Productimage.objects.filter(pid=product.id))
            # 对象 不支持json序列化   把python对象转化字典
            # pro = model_to_dict(product)
            li.append(product.to_dict())
        result.update(state=200, msg='成功', data=li)
    except BaseException as e:
        result.update(state=-1, msg='失败')
    return HttpResponse(json.dumps(result, cls=DjangoJSONEncoder), content_type='Application/json')


#接口2 一栏和二栏和轮播图
def get_category_data(request):
    """
        获取分类菜单的数据
        return:

    """
    result = {}
    try:
        cate_list = Category.objects.all()
        #轮播图
        banners = Banner.qs_to_dict(Banner.objects.all())
        #result字典中新增banner属性
        result.update(banners=banners)
        li = []
        for cate in cate_list:
            #select * from categorysub where cid=60,关联查询
            #利用外键关联, 查询子菜单数据
            sub_list = Categorysub.objects.filter(cid=cate.id)
            #将queryset对象转化成列表套字典的数据类型
            cate.subs = Category.qs_to_dict(sub_list)
            temp = cate.to_dict()
            li.append(temp)

        result.update(state=200,msg='success',data=li)
    except:
        #拼接数据
        result.update(state=404,msg="查询失败")
    return HttpResponse(json.dumps(result),content_type='Application/json')

#接口3 content文本框中数据
def get_shop_data(request):
    result = {}
    #保存分类信息的数据
    li = []
    try:
        #查看所有的category内容
        cates = Category.objects.all()
        for cate in cates:
            #Product.objects.filter(cid = category)
            #查询每个分类的商品信息
            products = cate.product_set.all()
            #遍历商品信息,通过商品对象来获取图片的信息
            for product in products:
                #product和图片表之间是一对多的关系
                #select * from productimage where pid=product.id
                #product新增一个属性aaa或者imgs（值得研究）
                product.imgs = BaseModel.qs_to_dict(product.product_image.all())
            #将商品信息添加到每个分类对象
            cate.products = BaseModel.qs_to_dict(products)
            #cate.to_dict()将python对象转换成为字典
            li.append(cate.to_dict())
            #data列表
        result.update(state=200,msg='success',data=li)
    except:
        result.update(state=404,msg='失败')
    return HttpResponse(json.dumps(result),content_type='Application/json')


