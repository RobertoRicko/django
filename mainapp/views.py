from django.shortcuts import render
import random
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
    with open('productlist.txt', encoding="UTF-8") as f:
        if len(productlist) < 1:
            for object in f:
                productlist.append(object.strip())
    context = {'products': productlist}
    return render(request, 'mainapp/products.html', context)
