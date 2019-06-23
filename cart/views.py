from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View

from .models import *
from .forms import *

def cart_home(request):
    return render(request, 'cart/cart_home.html', {})