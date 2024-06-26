from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100,null = True)
    email = models.CharField(max_length= 100 , null = True)
    phone = models.CharField(max_length= 100 , null = True)
    profile_pic = models.ImageField(null=True, blank= True)
    date_created = models.DateTimeField(auto_now_add=True,null= True)
    
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=100, null = True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    
    name = models.CharField(max_length = 100,null = True)
    price = models.FloatField(null= True)
    category = models.CharField(max_length = 100,choices= CATEGORY)
    description = models.CharField(max_length = 100, blank= True,null= True)
    date_created = models.DateTimeField(auto_now_add=True,null= True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name 
    

class Order(models.Model):
    
    STATUS = (
        ('Pending','Pending'),
        ('Out For Delivery','Out For Delivery'),
        ('Delivered','Delivered'),
    )
    
    customer = models.ForeignKey(Customer,null = True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null = True, on_delete= models.SET_NULL)
    stauts = models.CharField(max_length=100 , choices= STATUS)
    date_created = models.DateTimeField(auto_now_add=True,null= True)
    
    def __str__(self):
        return self.product