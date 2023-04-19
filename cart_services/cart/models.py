from django.db import models

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=1000, default="")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cart'
        ordering = ['-create_at']
    

class CartItem(models.Model):
    quantity = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # 1 product có thể chứa trong nhiều cart Item
    # ForeignKey: 1 - n
    productDetailUrl = models.CharField(max_length=200)
    cart_id = models.ForeignKey(Cart, unique=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart_items'
        ordering = ['-update_at']

    def __str__(self):
        return "{} - {} - {}".format(self.productDetailUrl,
                                               self.quantity,
                                               self.update_at)
        
    # def total(self):
    #     return self.quantity * self.product.price

    # def name(self):
    #     return self.product.name

    # def price(self):
    #     return self.product.price

    # def get_absolute_url(self):
    #     return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()
