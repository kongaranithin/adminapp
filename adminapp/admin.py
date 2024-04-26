from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid','pname','pcost','pmfdt','pexpdt']
    list_filter = ['pid','pmfdt','pexpdt']
    class meta:
        model=Product
admin.site.register(Product,ProductAdmin)

# Register your models here.
