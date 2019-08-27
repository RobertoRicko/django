from django.shortcuts import render
from .models import Product, ProductCategory

def main(request):
    return render(request, 'mainapp/main.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def products(request, pk=None):
    product_list = Product.objects.all()
    if pk:
        product_list = product_list.filter(category__pk=pk)
    context = {'products': product_list, 'categories': ProductCategory.objects.all, 'basket':request.user.basket.all()}
    return render(request, 'mainapp/products.html', context)