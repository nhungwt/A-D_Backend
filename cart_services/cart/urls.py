from django.urls import  path
from . import views

urlpatterns = [
    path('show_cart/', views.CartItemListView.as_view(), name='show_cart'),
    path('show_cart_item/<int:pk>', views.CartItemDetailView.as_view(), name='show_cart_item'),
    path('show_all_cart/', views.CartListView.as_view(), name='show_all_cart'),
]