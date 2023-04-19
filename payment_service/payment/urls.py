from django.urls import path
from . import views

urlpatterns = [
    path("orders/", views.OrderListView.as_view(), name="get_all_orders"),
    path("orders/<int:pk>", views.OrderItemListView.as_view(), name="get_all_order_items"),
    path(
        "order_item/<int:pk>/",
        views.OrderItemDetailView.as_view(),
        name="get_detail_order_item",
    ),
]
