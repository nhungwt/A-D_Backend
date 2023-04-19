import datetime
from django.shortcuts import render
from django.template import RequestContext
from . import cart as cartHandler
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


def get_cart_items(self, request):
    # cart_id = "" # Lấy từ cookie
    cart_id = cartHandler._cart_id(request)
    try:
        cart = Cart.objects.get(cart_id=cart_id)
        msg = "Lấy thành công cart_items"
    except Cart.DoesNotExist:
        cart = Cart(cart_id=cart_id)
        msg = "Cart vừa được khởi tạo"
        cart.save()
    cart_items = CartItem.objects.filter(cart_id=cart.id)
    return msg, cart_items


class CartListView(APIView):
    def get(self, request, format=None):
        try:
            cart = Cart.objects.all()
        except Cart.DoesNotExist:
            pass
        serializer = CartSerializer(cart, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class CartItemListView(APIView):
    def get(self, request, format=None):
        msg, cart_items = get_cart_items(request)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(
            {"msg": msg, "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request, format=None):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            # check to see if item is already in cart
            _, cart_items = get_cart_items(request)

            # TODO: Delete if not use anymore
            if cart_items.count() > 0:
                for cart_item in cart_items:
                    if (
                        cart_item.productDetailUrl
                        == serializer.data["productDetailUrl"]
                    ):
                        # update the quantity if found
                        cart_item.augment_quantity(serializer.data["quantity"])
            else:
                # if not product_in_cart:
                # create and save a new cart item
                ci = CartItem()
                ci.productDetailUrl = serializer.data["productDetailUrl"]
                ci.quantity = serializer.data["quantity"]
                token_cart = cartHandler._cart_id(request)
                ci.cart_id = Cart.objects.get(cart_id=token_cart)
                ci.save()
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemDetailView(APIView):
    def get(self, request, pk):
        cart_item = get_object_or_404(CartItem, pk=pk)
        serializer = CartItemSerializer(cart_item)
        return Response(
            {"msg": "Lấy thành công 1 item", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk):
        cart_item = get_object_or_404(CartItem, pk=pk)
        serializer = CartItemSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cart_item = get_object_or_404(CartItem, pk=pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
