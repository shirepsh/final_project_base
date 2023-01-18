from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.contrib.auth.models import User

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status

from .serializers import *
from .models import *

# //////////// test 
def home(request):
    return HttpResponse("hello")

#  /////////////// login 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# ///////////////// register
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = False
    user.save()
    return Response("new user born")

# /////////////////// full crud category authenticed using APIviews - just for admins
@api_view(["GET","POST","DELETE","PUT"])
def get_category(request,_id=-1):
    if request.method == "GET":
        if _id == -1:
            serializer = CategorySerializer(Category.objects.all(), many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            try:
                product = Category.objects.get(id=_id)
                serializer = CategorySerializer(Category.objects.get(id=_id))
            except:
                 return Response(status=status.HTTP_400_BAD_REQUEST, data="teacher nor found")
            return Response(status=status.HTTP_200_OK, data=serializer.data)


@api_view(["POST","DELETE","PUT"])
@permission_classes([IsAdminUser])
# @permission_classes([IsAuthenticated])
def change_category(request,_id=-1):
    if request.method == "POST":
        print(IsAdminUser)
        # create varabile with the serialixation type , if it valid we save it to the DB 
        new_category = CategorySerializer(data=request.data)
        if new_category.is_valid():
            new_category.save()
            return Response(status=status.HTTP_201_CREATED, data=new_category.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data="data not valid")

    # delete by id
    elif request.method == "DELETE":
        id_2_del = _id
        try:
            category = Category.objects.get(id=id_2_del)
            category.delete()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="category not found")
        return Response(status=status.HTTP_200_OK, data="category delete")

    # update by id
    elif request.method == "PUT":
        id_2_upd = _id
        try:
            ser = CategorySerializer(data=request.data)
            old_category = Category.objects.get(id=id_2_upd)
            res = ser.update(old_category, request.data)
            return HttpResponse(res, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="category nor found")

     























    
    

   
    
