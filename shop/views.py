from django.shortcuts import render
from .models import Product, Order
from django.core.paginator import Paginator
from django.urls import reverse

def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)

    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    context = {
        'product_object' : product_object,
    }
    return render(request, 'shop/index.html', context)

def detail(request, pk):
    product_object = Product.objects.get(pk=pk)
    return render(request, 'shop/detail.html', {'product' : product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get("items")
        name = request.POST.get('inputName')
        email = request.POST.get('inputEmail')
        address = request.POST.get('inputAddress')
        city = request.POST.get('inputCity')
        state = request.POST.get('inputState')
        zipCode = request.POST.get('zipcode')
        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipCode=zipCode)
        order.save()
    return render(request, 'shop/checkout.html')