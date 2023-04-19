# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrderListView(APIView):
    def get(self, request, format=None):
        try:
            order = Order.objects.all()
        except Order.DoesNotExist:
            pass
        serializer = OrderSerializer(order, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
        
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemListView(APIView):
    def get(self, request, pk, format=None):
        order = get_object_or_404(Order, pk=pk)
        try:
            order_items = order.orderitem_set.all()
        except OrderItem.DoesNotExist:
            pass
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request, pk, format=None):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemDetailView(APIView):
    def get(self, request, pk):
        order_item = get_object_or_404(OrderItem, pk=pk)
        serializer = OrderItemSerializer(order_item)
        return Response(
            {"data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk):
        order_item = get_object_or_404(OrderItem, pk=pk)
        serializer = OrderItemSerializer(order_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order_item = get_object_or_404(OrderItem, pk=pk)
        order_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






### This function is for fetching the user data.
# def get_transaction_details(uname):
#     user = paystat.objects.filter(username = uname)
#     for data in user.values():
#         return data

### This function is used for storing the data.
# def store_data(uname, prodid, price, quantity, mode_of_payment, mobile):
#     user_data = paystat(username = uname, product_id = prodid, price = price, quantity = quantity, mode_of_payment = mode_of_payment, mobile = mobile, status = "Success")
#     user_data.save()
#     return 1

### This function is created for getting/CREATE the payment.
# @csrf_exempt
# def get_payment(request):
    # uname = request.POST.get("User Name")
    # prodid = request.POST.get("Product id")
    # price = request.POST.get("Product price")
    # quantity = request.POST.get("Product quantity")
    # mode_of_payment = request.POST.get("Payment mode")
    # mobile = request.POST.get("Mobile Number")
    # resp = {}
    # if uname and prodid and price and quantity and mode_of_payment and mobile:
    #     ### It will call the store data function.
    #     respdata = store_data(uname, prodid, price, quantity, mode_of_payment, mobile)
    #     # respdata2 = ship_update(uname)
    #     ### If it returns value then will show success.
    #     if respdata:
    #         resp['status'] = 'Success'
    #         resp['status_code'] = '200'
    #         resp['message'] = 'Transaction is completed.'
    #     ### If it is returning null value then it will show failed.
    #     else:
    #         resp['status'] = 'Failed'
    #         resp['status_code'] = '400'
    #         resp['message'] = 'Transaction is failed, Please try again.'
    # ### If any mandatory field is missing then it will be through afailed message.
    # else:
    #     resp['status'] = 'Failed'
    #     resp['status_code'] = '400'
    #     resp['message'] = 'All fields are mandatory.'
    # return HttpResponse(json.dumps(resp), content_type = 'application/json')

### This function is created for getting the username and password.
# @csrf_exempt
# def user_transaction_info(request):
#     uname = request.POST.get("User Name")
#     if request.method == 'POST':
#         if 'application/json' in request.META['CONTENT_TYPE']:
#             val1 = json.loads(request.body)
#             uname = val1.get('User Name')
#             resp = {}
#             if uname:
#                 ## Calling the getting the user info.
#                 respdata = get_transaction_details(uname)
#                 if respdata:
#                     resp['status'] = 'Success'
#                     resp['status_code'] = '200'
#                     resp['data'] = respdata
#                 ### If a user is not found then it give failed as response.
#                 else:
#                     resp['status'] = 'Failed'
#                     resp['status_code'] = '400'
#                     resp['message'] = 'User Not Found.'
#                 ### The field value is missing.
#             else:
#                 resp['status'] = 'Failed'
#                 resp['status_code'] = '400'
#                 resp['message'] = 'Fields is mandatory.'
#         else:
#             resp['status'] = 'Failed'
#             resp['status_code'] = '400'
#             resp['message'] = 'Request type is not matched.'
#     else:
#         resp['status'] = 'Failed'
#         resp['status_code'] = '400'
#         resp['message'] = 'Request type is not matched.'
#     return HttpResponse(json.dumps(resp), content_type = 'application/json')

