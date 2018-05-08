from django.conf.urls import url

from home import views

urlpatterns = [
    url('search/', views.get_search_shop),
    url('category/', views.get_category_data),
    url('shop/',views.get_shop_data)
]