import logging
from django.conf import settings
from django.core.paginator import Paginator

from django.shortcuts import render

from shop.models import Product

# Create your views here.
logger = logging.getLogger(__name__)


def index(request):

    products_list = Product.objects.all()

    paginator = Paginator(products_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})

def product_details(request, product_id):
    product_details = Product.objects.get(id=product_id)
    return render(request, 'product_details.html', {'product_details': product_details})
