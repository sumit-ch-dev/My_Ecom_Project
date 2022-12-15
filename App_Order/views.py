from django.shortcuts import render, get_object_or_404, redirect

#Authentication
from django.contrib.auth.decorators import login_required

#Models
from App_Order.models import Cart, Order
from App_Shop.models import Product

#Messages
from django.contrib import messages

# Create your views here.


@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user,
    purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    print("order Qs")
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "this item quantity was updated")
            return redirect("App_Shop:home")
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "this item was added to your cart.")
            return redirect("App_Shop:home")
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, "This item was added to your cart.")
        return redirect('App_Shop:home')