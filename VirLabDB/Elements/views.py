from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Product

def hello_world(request):
    product = Product.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'products': product
    }
    return HttpResponse(template.render(context,request))
