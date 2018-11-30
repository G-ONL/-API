from django.contrib import admin
from payment.models import Payment, Payment_address

admin.site.register(Payment_address)
admin.site.register(Payment)


# Register your models here.
