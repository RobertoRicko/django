from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import BasketSlot
from mainapp.models import Product


def add(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.user.is_authenticated:
        basket_slot = request.user.basket.filter(product=product).first()
        if basket_slot:
            basket_slot.quantity += 1
            basket_slot.save()
        else:
            new_basket_slot = BasketSlot(user=request.user, product=product)
            new_basket_slot.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def remove(request, product_pk=None):
    product = get_object_or_404(Product, pk=product_pk)
    basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()

    if basket_slot:
        if basket_slot.quantity == 1:
            basket_slot.delete()
        else:
            basket_slot.quantity -= 1
            basket_slot.save()

    return HttpResponseRedirect(request.META('HTTP_REFERER'))