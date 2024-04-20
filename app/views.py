from django.shortcuts import render, redirect
from .models import Shop, Product


def home(request):
    return render(request, "index.html", {"shops": Shop.objects.all()})


def detailShop(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    if request.method == "POST":
        products = Product.objects.filter(shop=shop)
        return redirect("detail", shop_id=shop_id)
    products = Product.objects.filter(shop=shop)
    return render(request, "detail.html", {"shop": shop, "products": products})
