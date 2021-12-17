from typing import Pattern
from django.urls import path, include
from product import views

urlpatterns = [
    path('lastest-products', views.LatestProductList.as_view(), name='latest_product'),
    path('products/<slug:category_slug>/<slug:product_slug>', views.ProductDetail.as_view(), name='product_details'),
    path('products/<slug:category_slug>', views.CategoryDetail.as_view(), name='category_details')
]
