from django.shortcuts import render
from django.views import generic
from .helpers import (
    get_products, get_topmost_parent, get_children, 
    get_count_products, get_avg_price
)
# Create your views here.


class ProductsView(generic.View):
    """View which loads all the data from database added through Excel sheet"""

    def get(self, request):
        products = get_products()
        return render(request, 'products/index.html', {"products": products})


class ProductParentView(generic.View):
    """View for printing Parent product of a child product"""

    def get(self, request, product_code):
        parent = get_topmost_parent(product_code)
        return render(request, 'products/faq2.html', {"parent": parent})


class ProductChildrenView(generic.View):
    """View for Listing out Children of Parent Products"""

    def get(self, request, product_code):
        children = get_children(product_code)
        return render(request, 'products/faq3.html', {"children": children})


class ProductCountView(generic.View):
    """View for count of active and inactive products"""

    def get(self, request):
        data = get_count_products()
        return render(request, 'products/faq4.html', {"data": data})


class ProductAverageView(generic.View):
    """View for average between various types of products between category1 and category2"""

    def get(self, request):
        data = get_avg_price()
        return render(request, 'products/faq5.html', {"data": data})
