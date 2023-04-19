from .models import CartItem
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import decimal  # not needed yet but we will later
import random
CART_ID_SESSION_KEY = 'cart_id'

# Dấu (_) thể hiện đây là hàm private - trong python ko có nhưng nên ngầm hiểu với nhau như vậy
# get the current user's cart id, sets new one if blank
def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY, '') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]


def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id

# # return all items from the current user's cart
# def get_cart_items(request):
#     return CartItem.objects.filter(cart_id=_cart_id(request))

# # add an item to the cart
# def add_to_cart(request):
#     postdata = request.POST
#     # get product slug from post data, return blank if empty
#     product_slug = postdata.get('product_slug', '')
#     # get quantity added, return 1 if empty
#     quantity = postdata.get('quantity', 1)
#     # fetch the product or return a missing page error
#     p = get_object_or_404(Product, slug=product_slug)
#     # get products in cart
#     cart_products = get_cart_items(request)
#     product_in_cart = False
#     # check to see if item is already in cart
#     for cart_item in cart_products:
#         if cart_item.product.id == p.id:
#             # update the quantity if found
#             cart_item.augment_quantity(quantity)
#             product_in_cart = True
#     if not product_in_cart:
#         # create and save a new cart item
#         ci = CartItem()
#         ci.product = p
#         ci.quantity = quantity
#         ci.cart_id = _cart_id(request)
#         ci.save()

# # returns the total number of items in the user's cart
# def cart_distinct_item_count(request):
#     return get_cart_items(request).count()

# def get_single_item(request, item_id):
#     return get_object_or_404(CartItem, id=item_id, cart_id=_cart_id(request))

# # update quantity for single item
# def update_cart(request):
#     postdata = request.POST
#     item_id = postdata['item_id']
#     quantity = postdata['quantity']
#     cart_item = get_single_item(request, item_id)
#     if cart_item:
#         if int(quantity) > 0:
#             cart_item.quantity = int(quantity)
#             cart_item.save()
#         else:
#             remove_from_cart(request)

# # remove a single item from cart
# def remove_from_cart(request):
#     postdata = request.POST
#     item_id = postdata['item_id']
#     cart_item = get_single_item(request, item_id)
#     if cart_item:
#         cart_item.delete()

# # gets the total cost for the current cart
# def cart_subtotal(request):
#     cart_total = decimal.Decimal('0.00')
#     cart_products = get_cart_items(request)
#     for cart_item in cart_products:
#         cart_total += cart_item.product.price * cart_item.quantity
#     return cart_total



# #####################################################
# from .models import Cart
# # from shopping_cart_api.discounts.helpers import CampaignHelper, CouponHelper

# class CartHelper:

#     def __init__(self, user):
#         self.user = user
#         self.cart_base_total_amount = 0
#         self.cart_final_total_amount = 0
#         self.campaign_discount_amounts = []
#         self.campaign_discount_amount = 0
#         self.coupon_discount_amount = 0
#         self.delivery_cost = 0
#         self.cart_items = []
#         self.discounts = {}
#         self.checkout_details = {'products': [], 'total': [], 'amount': []}

#     def prepare_cart_for_checkout(self):
#         self.cart_items = Cart.objects.filter(user=self.user)

#         if not self.cart_items:
#             return False

#         self.calculate_cart_base_total_amount()
#         self.calculate_discount_amounts()
#         self.get_total_amount_after_discounts()
#         self.prepare_checkout_details()

#         return self.checkout_details

#     # def get_delivery_cost(self):
#     #     delivery_helper = DeliveryCostHelper(cart_items=self.cart_items)
#     #     self.delivery_cost = delivery_helper.calculate_delivery_cost()

#     def calculate_cart_base_total_amount(self):
#         for cart_item in self.cart_items:
#             self.cart_base_total_amount += cart_item.item.price * cart_item.quantity

#     # def get_coupon_discounts(self):
#     #     coupon_helper = CouponHelper(cart_total_amount=self.cart_base_total_amount)
#     #     self.discounts['coupons'] = coupon_helper.get_coupon_discounts()

#     # def get_campaign_discounts(self):
#     #     campaign_helper = CampaignHelper(self.cart_items)
#     #     self.discounts['campaigns'] = campaign_helper.get_campaign_discounts()

#     def calculate_discount_amounts(self):

#         try:
#             for discount in self.discounts.get('campaigns', []):
#                 if discount.discount_type == 'Amount':
#                     self.campaign_discount_amounts.append(discount.amount.get('amount'))

#                 if discount.discount_type == 'Rate':
#                     self.campaign_discount_amounts.append((self.cart_base_total_amount *
#                                                            discount.amount.get('rate')) / 100)

#             for discount in self.discounts.get('coupons', []):
#                 self.coupon_discount_amount = (self.cart_base_total_amount * discount.amount.get('rate')) / 100
#         except Exception as e:
#             print('Error when trying to calculating discount amounts {0}'.format(str(e)))

#     def get_total_amount_after_discounts(self):

#         if len(self.campaign_discount_amounts) > 0:
#             self.campaign_discount_amount = max(self.campaign_discount_amounts)

#         self.cart_final_total_amount = self.cart_base_total_amount - (
#                     self.campaign_discount_amount + self.coupon_discount_amount)

#         return self.cart_final_total_amount

#     def prepare_checkout_details(self):
#         for cart_item in self.cart_items:
#             self.checkout_details['products'].append({'category_id': cart_item.item.category.id,
#                                                       'category_name': cart_item.item.category.title,
#                                                       'product_id': cart_item.item.id,
#                                                       'product_name': cart_item.item.title,
#                                                       'quantity': cart_item.quantity,
#                                                       'unit_price': cart_item.item.price})

#         self.checkout_details['total'].append({'total_price': self.cart_base_total_amount,
#                                                'total_discount':
#                                                    self.campaign_discount_amount + self.coupon_discount_amount})

#         self.checkout_details['amount'].append({'total_amount': self.cart_final_total_amount,
#                                                 'delivery_cost': self.delivery_cost})