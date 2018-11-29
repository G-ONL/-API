from django.urls import path
from . import views


urlpatterns = [
    #product 조회
    path('', views.Product_search, name='product'),
]