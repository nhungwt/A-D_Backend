# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
# from cart_services.cart import cart


class CategoryListView(APIView):
    """
    Get list categories
    """
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 # TODO: Delete if not use anymore
# class CategoryDetailView(APIView):
#     # Get list products in a category
#     def get(self, request, slug, format=None):
#         category = get_object_or_404(Category, slug=slug)
#         response = requests.get(category.urlService)
#         product_list = json.loads(response.content.decode('utf-8'))
#         return Response(product_list, status=status.HTTP_200_OK)

    # def put(self, request, slug, format=None):
    #     category = get_object_or_404(Category, slug=slug)
    #     serializer = CategorySerializer(category, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, slug, format=None):
    #     category = get_object_or_404(Category, slug=slug)
    #     category.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductailDeaView(APIView):
#     """
#     Get list products in a category
#     """

#     def get(self, request, slug):
#         response = requests.get(category.urlService)
#         product_list = json.loads(response.content.decode('utf-8'))
#         return Response(product_list, status=status.HTTP_200_OK)
    
#      # Tạo mới
#     def post(self, request, format=None):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductDetailView(APIView):
#     def get_object(self, slug):
#         try:
#             return Product.objects.get(slug=slug)
#         except Product.DoesNotExist:
#             raise Http404
        
#     # Gọi để trả ra một loạt các cái sản phẩm
#     # Ví dụ gọi tới Book Service, nó sẽ trả ra '1 list các book'
#     def get(self, request, slug):
#         productService = get_object_or_404(Product, slug=slug)
#         response = requests.get(productService.urlService)
#         product_list = json.loads(response.content.decode('utf-8'))
#         return Response(product_list, status=status.HTTP_200_OK)
        

    # # Add product to cart
    # def post(self, request, slug):
    #     form = ProductAddToCartForm(request, request.POST)
    #     # check if posted data is valid
    #     if form.is_valid():
    #         # add to cart and redirect to cart page
    #         cart.add_to_cart(request)
    #         # if test cookie worked, get rid of it
    #         if request.session.test_cookie_worked():
    #             request.session.delete_test_cookie()
    #         # CHUYỂN HƯỚNG NGƯỜI DÙNG TỚI TRANG XEM CART, 'show_cart' là tên của url, ko phải tên hàm
    #         return redirect(reverse('show_cart'))

    #     # it’s a GET, create the unbound form. Note request as a kwarg
    #     form = ProductAddToCartForm(request=request, label_suffix=':')
    #     product = get_object_or_404(Product, slug=slug)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)

