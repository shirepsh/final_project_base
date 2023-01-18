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
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')

    def __str__(self):
        return self.name

# product model
class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    category = models.ForeignKey(Category, on_delete=models.PROTECT )


    def __str__(self):
        return self.name

# order model
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.IntegerField(null=False, blank=False, unique=True)
    product = models.ManyToManyField(Product)
    # quantity = models.IntegerField(null=False, blank=False)
    ordering_customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name = 'customer')
    shipping_country = models.CharField(max_length=255, null=False, blank=False)
    shipping_city = models.CharField(max_length=255, null=False, blank=False)
    shipping_zipCode = models.IntegerField(null=False, blank=False)

    def _str_(self):
        return str(self.ordering_customer)

# # class order items
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()


# review model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT, null = False)
    order_id = models.ForeignKey(Order, on_delete = models.PROTECT, null = False)
    productReview = models.ForeignKey(Product, on_delete = models.PROTECT, null = False)
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.CharField(max_length = 500, null = True)

    def _str_(self):
        return self.productReview