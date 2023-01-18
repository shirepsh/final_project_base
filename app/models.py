from django.db import models
from django.contrib.auth.models import User

# profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user

# category model
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')

    def __str__(self):
        return self.name


# product model
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    category = models.ForeignKey(Category, on_delete=models.PROTECT )

    def __str__(self):
        return self.name

# order model
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order_number = models.IntegerField(null=True, blank=True)
    ordering_customer = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, related_name = 'customer')
    customer_address = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True)
    quantity = models.IntegerField(null=True, blank=True)

    def _str_(self):
        return self.order_number


# # cart model
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(null=True, blank=True)

#     def __str__(self):
#         return self.user


    


