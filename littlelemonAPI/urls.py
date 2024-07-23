from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter




urlpatterns = [
    # can add category
    path('category/', views.CategoryView.as_view()),
    path('category/<int:pk>', views.SingleCategoryView.as_view()),
    # can add menu item
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleItemView.as_view()),
]
#     path('menu-items9',views.MenuItemClassViewSet.as_view({'get':'list'})),
#     path('menu-items9/<int:pk>',views.MenuItemClassViewSet.as_view({'get':'retrieve'})),

