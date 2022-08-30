from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    description = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    img = models.ImageField(upload_to='image',blank=True, null=True)
    slug = models.SlugField(unique=True, null=True)


    
    @property
    def ImageUrl(self):
        try:
            url= self.img.url
        except:
            url=''
        return url


    def __str__(self):
        return self.title


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    qunatity = models.IntegerField(default=1)
    ordered= models.BooleanField(default=False)
    added_date= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

  
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    ordered_date= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username










