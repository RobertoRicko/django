from django.shortcuts import render
import random
from .models import Product
productlist = []
namelist = []

def main(request):
    with open('nameslist.txt', encoding="UTF-8") as f:
        if len(namelist) < 1:
            for object in f:
                namelist.append(object.strip())
    context = {'guest_name': namelist[random.randrange(0,4)]}
    return render(request, 'mainapp/main.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', context)
