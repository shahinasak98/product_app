from django.urls import path
from .views import (
    ProductsView, ProductParentView, ProductChildrenView, ProductCountView, ProductAverageView
)

urlpatterns = [
    path('products/', ProductsView.as_view(), name="ProductsView"),
    path('faq2/<str:product_code>/', ProductParentView.as_view(), name="ProductsParentView"),
    path('faq3/<str:product_code>/', ProductChildrenView.as_view(), name="ProductsChildrenView"),
    path('count/', ProductCountView.as_view(), name="ProductCountView"),
    path('avg/', ProductAverageView.as_view(), name="ProductAvgView"),

]