from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)

    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    context = {
        'product_object' : product_object
    }
    return render(request, 'shop/index.html', context)