from django.conf.urls import url
from . import views


urlpatterns = [
    #payment create
    url('/', views.payment_create, name='payment'),
    #payment update
    #url('/', views.payment_update, name='payment_update'),
]