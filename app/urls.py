from django.urls import path
from . import viewsCategory
from . import viewsProducts
from . import viewsAuthentications

urlpatterns = [
    # authentication urls
    path('login', viewsAuthentications.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', viewsAuthentications.register),

    # category urls
    path('category', viewsCategory.get_category),
    path('category/<int:_id>', viewsCategory.get_category),
    path('changeCategory', viewsCategory.change_category),
    path('changeCategory/<int:_id>', viewsCategory.change_category),

    # products urls
    path('product', viewsProducts.get_products),
    path('product/<int:_id>', viewsProducts.get_products),
    path('changeProduct', viewsProducts.change_products),
    path('changeProduct/<int:_id>', viewsProducts.change_products)
]
