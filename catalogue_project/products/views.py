from django.shortcuts import render
from django.views import generic
from .models import Products
from .helpers import get_products, get_topmost_parent, get_children, count_products
# Create your views here.

class ProductsView(generic.View):
    def get(self,request):
        products = get_products()
        return render(request, 'products/index.html', {"products": products})
    
class ProductParentView(generic.View):
    def get(self, request, product_code):
        parent = get_topmost_parent(product_code)
        return render(request, 'products/faq2.html', {"parent": parent})

class ProductChildrenView(generic.View):
    def get(self, request, product_code):
        children = get_children(product_code)
        return render(request,'products/faq3.html',{"children": children} )

class ProductCountView(generic.View):
    def get(self, request):
        data = count_products()
        return render(request,'products/faq4.html',{"data": data} )

class ProductCountView(generic.View):
    def get(self, request):
        data = count_products()
        return render(request,'products/faq4.html',{"data": data} )
