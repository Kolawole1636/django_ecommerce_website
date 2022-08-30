from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<slug>', views.product, name='product'),
    path('about', views.about, name='about'),
    path('myproduct/Api', views.ProductList.as_view(), name='Api'),
     path('myproduct/Api/<int:pk>', views.ProductDetail.as_view(), name='ApiSingle'),
    
]
