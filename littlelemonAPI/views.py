from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
# for without serializer use:
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_csv.renderers import CSVRenderer
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage
from rest_framework.generics import RetrieveUpdateAPIView

# find a class-based view solution that allows for edit, deletion fields
# lab
# Can view and create new category item
class CategoryView(generics.ListCreateAPIView):
    queryset =Category.objects.all()
    serializer_class= CategorySerializer
# can edit category item by id
class SingleCategoryView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset =Category.objects.all()
    serializer_class= CategorySerializer

# adds filter button
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    # queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # serializer_class = MenuItemSerializer10
    ordering_fields=['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields=['category__title', 'title']
# can view, edit every menu item  
class SingleItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
        queryset = MenuItem.objects.all()
        serializer_class = MenuItemSerializer