from django.conf import settings
from django.db import models
from product.models import Category, Product
from  accounts.models import Customer


class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, 
                                on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"
    
    def get_total_item_price(self):
        return self.quantity * self.product.price
    

    def get_total_discount_item_price(self):
        return self.quantity * self.product.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    



class Order(models.Model):
    customer = models.ForeignKey(Customer, 
                                on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem, related_name="order_list",)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.customer.customer.username  

    def get_total(self):
        total = 0
        for order_item in self.products.all():
            total += order_item.get_final_price()
        return total