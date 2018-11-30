from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    #payment create
    path('', views.Payment_create, name='payment'),
    #payment update
    path('<int:payment_id>', views.Payment_update, name='payment_update'),
]