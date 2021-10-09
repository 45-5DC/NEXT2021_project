from django.contrib import admin
from .models import PurchasePost, PurchaseComment

# Register your models here.
admin.site.register(PurchasePost)
admin.site.register(PurchaseComment)