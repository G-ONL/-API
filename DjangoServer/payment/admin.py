from django.contrib import admin
from payment.models import Payment, Product, Payment_address
from AuthServer.models import Consumer, Seller

admin.site.register(Payment_address)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(Consumer)
admin.site.register(Seller)


# Register your models here.
