from django.contrib import admin
from . import models
from django.contrib.admin import AdminSite


@admin.register(models.Student)
class AdminProduct(admin.ModelAdmin):
    list_display = ('code','name', 'grade', 'mail')
    list_filter = ('grade')
