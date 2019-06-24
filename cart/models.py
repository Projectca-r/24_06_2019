from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed

from blog.models import *

# Create your models here.

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user_obj
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=True, null=True, blank=True)
    product_tv = models.ManyToManyField(Product_TV,
                                        blank=True,
                                        related_name='cart_tv')
    product_phone = models.ManyToManyField(Product_Phone,
                                           blank=True,
                                           related_name='cart_phone')
    product_a_laptop = models.ManyToManyField(Product_a_laptop,
                                              blank=True,
                                              related_name='cart_a_laptop')
    subtotal = models.DecimalField(max_digits=100,
                                   decimal_places=2,
                                   default=0.00)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


# =================================================================================
class Item_TV(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)
    product_tv = models.ManyToManyField(Product_TV,
                                        blank=True,
                                        related_name='item_tv')
    cart = models.ManyToManyField(Cart, blank=True, related_name='cart_tv')
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self(Product_TV.title)


# ==================================================================================
class Item_Phone(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)
    product_phone = models.ManyToManyField(Product_Phone,
                                           blank=True,
                                           related_name='item_phone')
    cart = models.ManyToManyField(Cart, blank=True, related_name='cart_phone')
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self(Product_Phone.title)


# ===================================================================================
class Item_a_laptop(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)
    product_a_laptop = models.ManyToManyField(Product_a_laptop,
                                              blank=True,
                                              related_name='item_a_laptop')
    cart = models.ManyToManyField(Cart,
                                  blank=True,
                                  related_name='cart_a_laptop')
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self(Product_a_laptop.title)
