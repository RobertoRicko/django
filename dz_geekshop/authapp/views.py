from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic.edit import UpdateView
from django.contrib import auth
from .forms import ShopUserRegisterForm

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    return render(request, 'authapp/login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    form = ShopUserRegisterForm()
    if request.method == "POST":
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    context = {'form': form}
    return render(request, 'authapp/register.html', context)


class EditView(UpdateView):
    pass