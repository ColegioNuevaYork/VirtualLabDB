from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.Product)
@admin.register(models.Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'brand', 'uncertainty', 'Available')
    list_filter = ('category',)
