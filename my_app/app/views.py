from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import HttpResponseForbidden
from django.db.models import Q
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = MyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your form has been successfully submitted")
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            form = MyForm(request.FILES)
    return render(request, 'home.html')