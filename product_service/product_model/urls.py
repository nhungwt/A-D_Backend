from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name = "categories"),
    # path("categories/<slug:slug>/", views.CategoryDetailView.as_view(), name = "category"),
    # path("products/<slug:slug>/", views.ProductDetailView.as_view(), name = "get_productService_detail"),
]