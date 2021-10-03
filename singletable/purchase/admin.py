from django.contrib import admin
from .models import Purchase, PurchaseComment

# Register your models here.
admin.site.register(Purchase)
admin.site.register(PurchaseComment)