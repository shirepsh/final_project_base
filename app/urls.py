from django.urls import path
from . import viewsCategory
from . import viewsProducts

urlpatterns = [
    # general urls
    path('login', viewsCategory.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', viewsCategory.register),
    path('', viewsCategory.home),

    # category urls
    path('category', viewsCategory.get_category),
    path('category/<int:_id>', viewsCategory.get_category),
    path('changeCategory/<int:_id>', viewsCategory.change_category),
    path('changeCategory', viewsCategory.change_category),

    # products urls
    path('product', viewsProducts.get_products),
    path('product/<int:_id>', viewsProducts.get_products),
    path('changeProduct/<int:_id>', viewsProducts.change_products),
    path('changeProduct', viewsProducts.change_products)
]
