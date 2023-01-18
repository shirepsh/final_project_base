from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAdminUser
from rest_framework import status

from .serializers import *
from .models import *

# /////////////////// full crud products - when post, delete, put just for admins
@api_view(["GET"])
def get_products(request,_id=-1):
    if request.method == "GET":
        if _id == -1:
            serializer = ProductSerializer(Product.objects.all(), many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            try:
                serializer = ProductSerializer(Product.objects.get(id=_id))
            except:
                 return Response(status=status.HTTP_400_BAD_REQUEST, data="product not found")
            return Response(status=status.HTTP_200_OK, data=serializer.data)


@api_view(["POST","DELETE","PUT"])
@permission_classes([IsAdminUser])
def change_products(request,_id=-1):
    if request.method == "POST":
        # create varabile with the serialixation type , if it valid we save it to the DB 
        new_product = ProductSerializer(data=request.data)
        if new_product.is_valid():
            new_product.save()
            return Response(status=status.HTTP_201_CREATED, data=new_product.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data="data not valid")

    # delete by id
    elif request.method == "DELETE":
        id_2_del = _id
        try:
            product = Product.objects.get(id=id_2_del)
            product.delete()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="product not found")
        return Response(status=status.HTTP_200_OK, data="product delete")

    # update by id
    elif request.method == "PUT":
        id_2_upd = _id
        try:
            ser = ProductSerializer(data=request.data)
            old_product = Product.objects.get(id=id_2_upd)
            res = ser.update(old_product, request.data)
            return HttpResponse(res, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="product nor found")

     























    
    

   
    
