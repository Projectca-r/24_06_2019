from .views import *
from django.urls import path

urlpatterns = [
    path('', home),
    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view),
]