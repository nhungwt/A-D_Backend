# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# class ĐƠn hàng
class Order(models.Model):
    customer_id = models.IntegerField() # Lấy 'token_access' sau đó lấy 'id' của Khách
    create_at = models.DateTimeField(auto_now_add=True)
    total_payment = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    # custom_address = models.CharField(max_length=200) # TODO: Để sau, bao giờ viết cái user_info đã
    
    class Meta:
        db_table = 'order'
        ordering = ['customer_id', '-create_at']
    
    def __str__(self):
        return "{} - {} - {}".format(self.create_at,
                                        self.total_payment)
        

class OrderItem(models.Model):
    product = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    order = models.ForeignKey(Order, unique=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order_item'
        ordering = ['product']

    def __str__(self):
        return "{} - {} - {}".format(self.product,
                                        self.quantity,
                                        self.price)

