# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from AuthServer import views

urlpatterns = [
    # 판매자 회원 가입
    path('seller/signup', views.seller_signup),

    # 판매자 로그인
    path('seller/signin', views.seller_signin),

    # [POST] /users/consumer/signup
    # 구매자의 회원가입을 담당한다
    path('consumer/signup', views.consumer_signup),

    # [POST] /users/consumer/signin
    # 구매자의 로그인을 담당한다
    path('consumer/signin', views.consumer_signin),

]