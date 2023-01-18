# from .models import *
# from rest_framework.response import Response


# def create_order(request):
#     customer1 = Customer.objects.create(name='lidor')
#     product1 = Product.objects.create(name='aaa', price=6.90)
#     product2 = Product.objects.create(name='bbb', price=8 )

#     order = Order.objects.create(customer=customer1)
#     order.products.add(product1, through_defaults={'quantity': 2})
#     order.products.add(product2, through_defaults={'quantity': 3})

#     return Response("success")