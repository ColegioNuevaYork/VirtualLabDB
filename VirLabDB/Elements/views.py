from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Product

def hello_world(request):
    product = Product.objects.order_by('id')
    template = loader.get_template('test.html')
    context = {
        'products': product
    }
    return HttpResponse(template.render(context, request))

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template = loader.get_template('productDetail.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))
