from django.contrib import admin
from .models.Customer import Customer
from .models.Complain import Complain

# Register your models here.
admin.site.register(Customer)
admin.site.register(Complain)
