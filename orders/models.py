from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.TextField(max_length=100)
    number = models.TextField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('name', 'number',)

class Order(models.Model):
    customer = models.ForeignKey(Customer,related_name="orders",on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True,blank=True)


class Item(models.Model):
    salwar_length = models.TextField(max_length=8, null=True, blank=True)
    salwar_shoulder = models.TextField(max_length=8, null=True, blank=True)
    salwar_chest = models.TextField(max_length=8, null=True, blank=True)
    salwar_waist = models.TextField(max_length=8, null=True, blank=True)
    salwar_neck = models.TextField(max_length=8, null=True, blank=True)
    salwar_sleeve = models.TextField(max_length=8, null=True, blank=True)
    salwar_bottom = models.TextField(max_length=8, null=True, blank=True)
    blouse_length = models.TextField(max_length=8, null=True, blank=True)
    blouse_shoulder = models.TextField(max_length=8, null=True, blank=True)
    blouse_chest = models.TextField(max_length=8, null=True, blank=True)
    blouse_waist = models.TextField(max_length=8, null=True, blank=True)
    blouse_neck = models.TextField(max_length=8, null=True, blank=True)
    blouse_sleeve = models.TextField(max_length=8, null=True, blank=True)
    blouse_bottom = models.TextField(max_length=8, null=True, blank=True)
    note = models.TextField(max_length=200, null=True, blank=True)
    image=models.TextField(max_length=500, null=True, blank=True)
    order = models.ForeignKey(Order,related_name="items", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=75, null=True, blank=True)


    