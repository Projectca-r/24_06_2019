from django.urls import path
from .views import *

urlpatterns = [
    path('', catalog_list, name='catalog_list_url'),
    path('catalog/<str:slug>/', CatalogDetail.as_view(), name='catalog_detail_url'),
# ==================================================================================
    # ---------------------------------------------------------------------------
# ================================ Category ==========================================
    path('category_tv/', category_tvs_list, name='category_tv_list_url'),
    path('category_tv/<str:slug>/', Category_TVDetail.as_view(), name='category_tv_detail_url'),
# --------------------------------------------------------------------------
    path('category_phone/', category_phones_list, name='category_phone_list_url'),
    path('category_phone/<str:slug>/', Category_PhoneDetail.as_view() , name='category_phone_detail_url'),
# --------------------------------------------------------------------------
    path('category_a_laptop/', category_a_laptops_list, name='category_a_laptop_list_url'),
    path('category_a_laptop/<str:slug>/', Category_a_laptopDetail.as_view(), name='category_a_laptop_detail_url'),
# ================================= Product =========================================
    path('product_tv/', product_tvs_list, name='product_tv_list_url'),
    path('product_tv/<str:slug>/', Product_TVDetail.as_view(), name='product_tv_detail_url'),
# -----------------------------------------------------------------------------------
    path('product_phone/', product_phones_list, name='product_phone_list_url'),
    path('product_phone/<str:slug>/', Product_PhoneDetail.as_view(), name='product_phone_detail_url'),
# -----------------------------------------------------------------------------------
    path('product_a_laptop/', product_a_laptops_list, name='product_a_laptop_list_url'),
    path('product_a_laptop/<str:slug>/', Product_a_laptopDetail.as_view(), name='product_a_laptop_detail_url'),
# ========================================================================================================
]