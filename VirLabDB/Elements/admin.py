from django.contrib import admin
from django.contrib.admin import AdminSite
from . import models
from django.utils.translation import ugettext_lazy

# Register your models here.
# admin.site.register(models.Product)
@admin.register(models.Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'brand','quantity','image','Available')
    list_filter = ('category',)
