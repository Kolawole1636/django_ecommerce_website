from re import search
from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import generics,filters
from .serializer import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]

    filterset_fields=["id","title","category"]
    search_fields=["id","title","category"]
    ordering_fields=["id","title","category"]





class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset= Product.objects.all()
     serializer_class= ProductSerializer
     














@login_required(login_url='login')
def home(request):

    items = Product.objects.all()
    context = {'myitems':items}

    return render(request, 'home.html',context)




def product(request, slug):
    item = Product.objects.get(slug=slug)
    context = {'item':item}

    return render(request, 'product.html',context)


def about(request):

    return render(request, 'about.html')


    









