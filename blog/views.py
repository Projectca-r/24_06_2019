from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
# from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import *
from .utils import *

# Create your views here.


# def Функция просмотра или вид для краткости, это просто функция,
#  которая принимает Python веб - запрос и возвращает веб - ответ.
def catalog_list(request):
    catalogs = Catalog.objects.all()
    context = {
        'catalogs': catalogs,
    }
    return render(request, 'blog/catalog_list.html', context=context)


class CatalogDetail(ObjectDetailMixin, View):
    model = Catalog
    template = 'blog/catalog_detail.html'


# ===========================================================================

# ==================================category=================================
# ----------------------------------TV---------------------------------


def category_tvs_list(request):
    category_tvs = Category_TV.objects.all()
    context = {
        'category_tvs': category_tvs,
    }
    return render(request, 'blog/tv/category_tv_list.html', context=context)


class Category_TVDetail(ObjectDetailMixin, View):
    model = Category_TV
    template = 'blog/tv/category_tv_detail.html'


# =============================================================================
# ---------------------Phone---------------------------------------------------


def category_phones_list(request):
    category_phones = Category_Phone.objects.all()
    context = {
        'category_phones': category_phones,
    }
    return render(request,
                  'blog/phone/category_phone_list.html',
                  context=context)


class Category_PhoneDetail(ObjectDetailMixin, View):
    model = Category_Phone
    template = 'blog/phone/category_phone_detail.html'


# ================================================================================
# ---------------------------a_laptop-----------------------------------------------


def category_a_laptops_list(request):
    category_a_laptops = Category_a_laptop.objects.all()
    context = {
        'category_a_laptops': category_a_laptops,
    }
    return render(request,
                  'blog/a_laptop/category_a_laptop_list.html',
                  context=context)


class Category_a_laptopDetail(ObjectDetailMixin, View):
    model = Category_a_laptop
    template = 'blog/a_laptop/category_a_laptop_detail.html'


# =============================== Product =======================================
# +++++++++++++++++++++++++++++++++ tv ++++++++++++++++++++++++++++++++++++++++++


def product_tvs_list(request):
    product_tvs = Product_TV.objects.all()
    context = {
        'product_tvs': product_tvs,
    }
    return render(request, 'blog/tv/product_tv_list.html', context=context)


class Product_TVDetail(ObjectDetailMixin, View):
    model = Product_TV
    template = 'blog/tv/product_tv_detail.html'


# ==============================================================================
# ---------------------------- phone -------------------------------------------


def product_phones_list(request):
    product_phones = Product_Phone.objects.all()
    context = {
        'product_phones': product_phones,
    }
    return render(request,
                  'blog/phone/product_phone_list.html',
                  context=context)


class Product_PhoneDetail(ObjectDetailMixin, View):
    model = Product_Phone
    template = 'blog/phone/product_phone_detail.html'


# ==============================================================================
# -------------------------------- a_laptop ------------------------------------


def product_a_laptops_list(request):
    product_a_laptops = Product_a_laptop.objects.all()
    context = {
        'product_a_laptops': product_a_laptops,
    }
    return render(request,
                  'blog/a_laptop/product_a_laptop_list.html',
                  context=context)


class Product_a_laptopDetail(ObjectDetailMixin, View):
    model = Product_a_laptop
    template = 'blog/a_laptop/product_a_laptop_detail.html'


# =================================== Cart ===========================================
